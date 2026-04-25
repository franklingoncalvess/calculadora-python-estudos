async function calcular(operacao) {
  const num1 = document.getElementById('num1').value;
  const num2 = document.getElementById('num2').value;

  try {
    let url = `http://localhost:8000/${operacao}?num1=${num1}&num2=${num2}`;
    const response = await fetch(url);
    const data = await response.json();

    if (data.resultado) {
      document.getElementById('resultado').innerText = `Resultado: ${data.resultado}`;
    } else {
      document.getElementById('resultado').innerText = `Erro: ${data.erro}`;
    }
  } catch (error) {
    document.getElementById('resultado').innerText = `Erro: ${error}`;
  }
}

async function calcularSoma() {
    calcular('soma');
}

async function calcularSubtracao() {
    calcular('subtracao');
}

async function calcularMultiplicacao() {
    calcular('multiplicacao');
}

async function calcularDivisao() {
    calcular('divisao');
}
