function mostrarMensagem() {
    alert("Olá, sou juliana, fico grata que queira ver meu linkedIn.")
}

function verificandoNumero() {

    let numero = document.getElementById("numero").value
    numero = Number(numero);
    let mensagem = ""

    if (numero == 0) {
        mensagem = "Número neutro"
    } else if (numero > 0) {
        mensagem = "Número positivo"
    } else {
        mensagem = "Número negativo"
    }

document.getElementById("resultado").innerText = mensagem
};

function executarFor(){
    let resultado = "Número pares 0 a 10 \n -> \n";

    for (let i = 0; i <=10; i++){
        if(i % 2 === 0){
           resultado += i + '\n';
        }

    }

    document.getElementById("saída").textContent = resultado
}

function executarArray(){
    let nomes = ["Manu", "Samara", "Andreia", "Ana"];
    let resultado = "Lista de Alunas: \n"

    for(i = 0; i < nomes.length; i++){
        resultado += nomes[i] + '\n';
    }

    document.getElementById("saida").textContent = resultado;
}
