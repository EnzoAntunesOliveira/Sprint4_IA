## Resumo

Este projeto utiliza Inteligência Artificial (IA) para identificar possíveis fraudes em consultas odontológicas. O sistema analisa padrões de atendimento e custos para detectar anomalias que possam indicar sinistros fraudulentos. Além disso, o projeto conta com uma interface web simples feita com Flask, onde é possível fazer o upload de um arquivo CSV contendo os dados de treinamento e visualizar os resultados do modelo de classificação diretamente na tela.

## Objetivos

- **Desenvolver um modelo de IA:** Utilizar algoritmos de aprendizado de máquina (como Random Forest) para sinalizar consultas suspeitas.
- **Detecção de fraudes:** Analisar padrões de custo e frequência de consultas para identificar sinistros potencialmente fraudulentos.
- **Painel de monitoramento:** Exibir os alertas e métricas (acurácia, relatório de classificação, matriz de confusão) de forma clara e organizada.
- **Avaliação de desempenho:** Implementar métricas (precision, recall, f1-score e suporte) para garantir a confiabilidade do modelo.

## Tecnologias Utilizadas

- **Linguagem:** Python
- **Bibliotecas e Frameworks:**
  - **Flask:** Para o back-end e criação da API web.
  - **scikit-learn:** Para criação, treinamento e avaliação do modelo de IA.
  - **pandas** e **numpy:** Para manipulação e limpeza dos dados.
  - **matplotlib** e **seaborn:** Mencionadas para visualização futura dos dados e análises mais aprofundadas.
- **Banco de Dados:** Utiliza arquivos CSV para armazenamento dos dados (com possibilidade de integração com SQL/MongoDB no futuro).
- **Ferramentas de Versionamento:** Git/GitHub

## Instalação e Configuração

1. **Clone o repositório ou crie a estrutura:**
   Se estiver começando do zero, crie a pasta `Sprint4_IA`

2. **Crie e ative um ambiente virtual:**
   No terminal, dentro da pasta do projeto, execute:
```bash
   python -m venv venv
   ```
**Ative o ambiente:**
```bash
   venv\Scripts\activate
   ```
1. **Instale as dependências:**
    
    Certifique-se de ter o arquivo `requirements.txt` com o seguinte conteúdo:
    
    ```
    Flask
    pandas
    numpy
    scikit-learn
    
    ```
    
    Em seguida, execute:
    
    ```bash
    pip install -r requirements.txt
    
    ```
    
2. **Atualize o pip (opcional):**
Caso precise atualizar o pip:
    
     ```bash
    python -m pip install --upgrade pip
     ```
    

## Rodando a Aplicação

1. **Inicie o servidor Flask:**
    
    Com o ambiente virtual ativo, execute:
    
    ```bash
    python app.py
    ```
    
    Isso iniciará o Flask, geralmente acessível em http://127.0.0.1:5000.
    
2. **Utilize a interface web:**
    - Abra o navegador e acesse http://127.0.0.1:5000.
    - Faça o upload do seu arquivo CSV contendo os dados de treinamento.
    - Após o envio, a aplicação processará os dados, treinará o modelo e exibirá os resultados:
         - **Acurácia:** Valor numérico que indica o desempenho global do modelo.
         - **Relatório de Classificação:** Mostra as métricas **precision**, **recall**, **f1-score** e **support** para cada classe.
         - **Matriz de Confusão:** Exibida como uma tabela estilizada que compara os valores reais e os valores previstos pelo modelo.

## Explicação dos Resultados

### Relatório de Classificação

O relatório é gerado pela função `classification_report` do scikit-learn e inclui:

- **Precision (Precisão):** Proporção de previsões corretas feitas para cada classe.
- **Recall (Revocação):** Proporção de verdadeiros positivos identificados.
- **F1-Score:** Média harmônica entre precision e recall.
- **Support:** Número de ocorrências reais para cada classe.

### Matriz de Confusão

A matriz de confusão compara os valores reais com os valores previstos pelo modelo. Por exemplo:

```
[[45, 24],
 [24, 7]]

```

- **Linha 1 (Real: 0):** Mostra os casos da classe 0 corretamente classificados e aqueles incorretamente classificados como classe 1.
- **Linha 2 (Real: 1):** Mostra os casos da classe 1, destacando os acertos e os erros de classificação.

## Futuras Melhorias e Expansões

- **Integração com Banco de Dados:** Migrar os dados dos CSVs para um banco de dados (SQL ou MongoDB) para escalabilidade.
- **Dashboard Interativo:** Desenvolver um painel mais robusto com gráficos interativos para monitoramento dos alertas em tempo real.
- **Modelos Mais Avançados:** Explorar redes neurais com TensorFlow ou PyTorch para aprimorar as análises preditivas.
- **Testes Automatizados:** Implementar testes para validação e melhoria contínua do modelo.

## **Autores:**

- Arthur Fenili RM 552752
- Enzo Antunes Oliveira RM 553185
- Vinicío Raphael RM 553813
