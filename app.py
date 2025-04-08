from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400
    
    file = request.files['file']
    
    try:
        data = pd.read_csv(file)
    except Exception as e:
        return jsonify({'error': 'Erro ao ler o CSV: ' + str(e)}), 400

    # Garantir que 'CUSTO_CONSULTA' esteja no formato numérico
    data['CUSTO_CONSULTA'] = pd.to_numeric(data['CUSTO_CONSULTA'], errors='coerce')
    data['CUSTO_CONSULTA'].fillna(data['CUSTO_CONSULTA'].mean(), inplace=True)

    # Converter 'DATA_CONSULTA' para data
    data['DATA_CONSULTA'] = pd.to_datetime(data['DATA_CONSULTA'], format='%d/%m/%Y', errors='coerce')

    # Limites de preço para tratamentos
    pricing_limits = {
        "Restauração Dentária": (150, 1800),
        "Tratamento de Canal": (250, 1000),
        "Tratamento Periodontal": (350, 1500),
        "Implantodontia": (1500, 3000),
        "Clareamento Dental": (400, 700)
    }

    def cost_out_of_range(row):
        treatment_type = row['DESCRICAO_TRATAMENTO']
        cost = row['CUSTO_CONSULTA']
        if treatment_type in pricing_limits:
            min_price, max_price = pricing_limits[treatment_type]
            if cost < min_price or cost > max_price:
                return 1
        return 0

    data['OUT_OF_RANGE'] = data.apply(cost_out_of_range, axis=1)

    # Calcular dias desde a última consulta para o mesmo paciente
    data = data.sort_values(by=['CPF', 'DATA_CONSULTA'])
    data['DAYS_SINCE_LAST'] = data.groupby('CPF')['DATA_CONSULTA'].diff().dt.days.fillna(9999)
    data['RECENT_CONSULTATION'] = np.where(data['DAYS_SINCE_LAST'] <= 2, 1, 0)

    # Codificar tratamentos e dentistas
    le_treatment = LabelEncoder()
    le_dentist = LabelEncoder()
    data['TREATMENT_ENCODED'] = le_treatment.fit_transform(data['DESCRICAO_TRATAMENTO'])
    data['DENTIST_ENCODED'] = le_dentist.fit_transform(data['NOME_DENTISTA'])

    # Selecionar variáveis e alvo
    try:
        X = data[['CUSTO_CONSULTA', 'OUT_OF_RANGE', 'RECENT_CONSULTATION', 'TREATMENT_ENCODED', 'DENTIST_ENCODED']]
        y = data['SINISTRO']
    except Exception as e:
        return jsonify({'error': 'Erro ao selecionar as variáveis. Verifique se as colunas necessárias existem. ' + str(e)}), 400

    # Dividir os dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Inicializar e treinar o modelo Random Forest
    rf_model = RandomForestClassifier(random_state=42, n_estimators=100, max_depth=10)
    rf_model.fit(X_train, y_train)
    y_pred = rf_model.predict(X_test)

    # Avaliar o modelo
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)

    return jsonify({
        'accuracy': accuracy,
        'report': report,
        'conf_matrix': conf_matrix.tolist()  # Converter para lista para serialização
    })

if __name__ == '__main__':
    app.run(debug=True)
