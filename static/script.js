// Função para renderizar a matriz de confusão como uma tabela HTML
function renderConfusionMatrix(matrix) {
    let html = '<table class="confusion-table"><thead><tr><th></th><th>Previsto: 0</th><th>Previsto: 1</th></tr></thead><tbody>';
    // Se for uma matriz 2x2, colocamos as classes reais também:
    html += `<tr><th>Real: 0</th><td>${matrix[0][0]}</td><td>${matrix[0][1]}</td></tr>`;
    html += `<tr><th>Real: 1</th><td>${matrix[1][0]}</td><td>${matrix[1][1]}</td></tr>`;
    html += '</tbody></table>';
    return html;
  }
  
  document.getElementById('upload-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    const fileInput = document.getElementById('csv-file');
    if (fileInput.files.length === 0) {
      alert("Por favor, selecione um arquivo CSV.");
      return;
    }
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);
    
    try {
      const response = await fetch('/upload', { method: 'POST', body: formData });
      const data = await response.json();
      document.getElementById('result').innerHTML = `
        <h2>Resultados:</h2>
        <p><strong>Acurácia:</strong> ${data.accuracy}</p>
        <h3>Relatório de Classificação:</h3>
        <pre class="classification-report">${data.report}</pre>
        <h3>Matriz de Confusão:</h3>
        ${renderConfusionMatrix(data.conf_matrix)}
      `;
    } catch (error) {
      console.error(error);
      alert("Erro ao processar o arquivo.");
    }
  });
  