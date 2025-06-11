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

document.getElementById("resultado").innerHTML = mensagem
}
