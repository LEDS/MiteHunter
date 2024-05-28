// Alert Verification

// Conta os arquivos e verifica se é compatível com a quantidade indicada
function countFiles(event) {
    var files = document.getElementById('myfile').files;
    var qntPics = {{ qntPics }};
    if (files.length < qntPics) {
        var confirmMessage = 'Você selecionou ' + files.length + ' fotos. A quantidade sugerida é ' + qntPics + '. Deseja continuar?';
        if (!confirm(confirmMessage)) {
            event.preventDefault();  // Impede o envio do formulário se o usuário cancelar
        }
    }
}

document.addEventListener('DOMContentLoaded', function() {
    var uploadButton = document.getElementById('uploadButton');
    uploadButton.addEventListener('click', countFiles);
});



// Navigation

//
function myFunction() {
var x = document.getElementById("mynav");
if (x.classList.contains("responsive")) {
    x.classList.remove("responsive");
} else {
    x.classList.add("responsive");
}
}



// carousel.js

// Função para carregar as imagens no carrossel
function loadCarouselImages(files) {
    var carouselIndicators = document.getElementById('carouselIndicators');
    var carouselInner = document.getElementById('carouselInner');

    // Limpar carrossel
    carouselIndicators.innerHTML = '';
    carouselInner.innerHTML = '';

    // Adicionar cada imagem selecionada ao carrossel
    for (var i = 0; i < files.length; i++) {
        var indicator = document.createElement('li');
        indicator.setAttribute('data-target', '#carouselExampleIndicators');
        indicator.setAttribute('data-slide-to', i);
        if (i === 0) {
            indicator.classList.add('active');
        }
        carouselIndicators.appendChild(indicator);

        var item = document.createElement('div');
        item.classList.add('carousel-item');
        if (i === 0) {
            item.classList.add('active');
        }
        var img = document.createElement('img');
        img.classList.add('d-block');
        img.classList.add('w-100');
        img.src = URL.createObjectURL(files[i]); // Criar URL para a imagem
        item.appendChild(img);
        carouselInner.appendChild(item);
    }

    // Ativar o carrossel
    $('.carousel').carousel();
}

// Event listener para o envio do formulário
document.getElementById('uploadForm').addEventListener('submit', function(event) {
    // Evitar que o formulário seja enviado automaticamente pelo JavaScript
    event.preventDefault(); 

    // Obter os arquivos selecionados
    var files = document.getElementById('myfile').files;
    
    // Carregar as imagens no carrossel
    loadCarouselImages(files);

    // Enviar o formulário manualmente após a manipulação das imagens
    this.submit();
});

// Event listener para o botão de visualizar o carrossel
document.getElementById('showCarouselButton').addEventListener('click', function(event) {
    // Obter os arquivos selecionados
    var files = document.getElementById('myfile').files;

    // Carregar as imagens no carrossel
    loadCarouselImages(files);
});