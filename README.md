<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/LEDS/MiteHunter">
    <img src="https://github.com/othneildrew/Best-README-Template/blob/master/images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">MiteHunter</h3>

  <p align="center">
    Monitoramento de pragas em culturas de morango
    <br />
    <a href="https://github.com/LEDS/MiteHunter"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/LEDS/MiteHunter">View Demo</a>
    ·
    <a href="mailto:mitehunter.leds@gmail.com?subject=BugReport">Report Bug</a>
    ·
    <a href="mailto:mitehunter.leds@gmail.com?subject=RequestFeature">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Sumário:</summary>
  <ol>
    <li>
      <a href="#about-the-project">Sobre o Projeto</a>
      <ul>
        <li><a href="#built-with">Tecnologias</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Começando</a>
      <ul>
        <li><a href="#prerequisites">pré-Requisitos</a></li>
        <li><a href="#installation">Instalando</a></li>
      </ul>
    </li>
    <li><a href="#usage">Uso</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contribuir</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contato</a></li>
    <li><a href="#acknowledgments">Agradecimentos</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Sobre o Projeto

[![Budibase][product-screenshot]]()

Neste projeto, estamos desenvolvendo um sistema web inteligente para identificação de infestação por ácaros rajados (Tetranychus urticae) em culturas de morango, utilizando fotos capturadas por smartphones como entrada. Atualmente, nossa aplicação está hospedada em um contêiner Budibase no Docker e pode ser acessada via HTTP na porta 10000.



### Tecnologias

* [![Python][Python.js]][Python-url]
* [![Django][Django.js]][Django-url]
* [![Docker][Docker.js]][Docker-url]
* [![Budibase][Budibase.js]][Budibase-url]



<!-- GETTING STARTED -->
## Começando

Para executar uma versão local do nosso projeto, siga o passo-a-passo abaixo.

### Pré-requisitos:
  - Docker: Certifique-se de ter o Docker instalado em seu sistema.
  - Clonar o repositório.

### Configuração:
1. Para configurar o docker, na pasta em que o repositório foi clonado, e na pasta **Infra/** abra o terminal e execute ```docker-compose up -d``` . <br><br>
2. Após o download e instalação, acesse o phpmyadmin em ```localhost:8081```. Selecionando o database **Inventario**, na aba **Importar**, selecione o arquivo ```DB_MiteHunter_clean.sql``` e confirme no botão **Importar**. <br><br>
3. Em ```localhost:10000```, que é onde está o budibase, você será redirecionado para uma tela de cadastro. Insira um email e senha de sua preferencia e use essas credenciais para logar no aplicativo. Após escolher o nome da aplicação, na aba superior selecione **Settings** e em seguida **Export/Import**, e importe o arquivo ```BudibaseStable.tar.gz``` disponível em **Infra/**.



<!-- USAGE EXAMPLES -->
## Uso
O Sistema de Gestão de Cultivos fornece uma interface web intuitiva para gerenciar informações relacionadas ao cultivo de plantas e colheitas. Após iniciar a aplicação, você pode acessá-la usando um navegador da web e começar a usar as funcionalidades disponíveis.


<!-- 

## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

-->


<!-- CONTRIBUTING -->
## Contribuindo

Contribuições são o que fazem da comunidade de código aberto um lugar tão incrível para aprender, inspirar e criar. Todas as contribuições que você fizer são **muito apreciadas**.

Se você tiver uma sugestão que possa melhorar isso, por favor, faça um fork do repositório e crie uma solicitação pull. Você também pode simplesmente abrir uma issue com a tag "melhoria".
Não se esqueça de dar uma estrela para o projeto! Obrigado novamente!

1. Faça um Fork do Projeto
2. Crie sua Branch de Recurso (`git checkout -b feature/AmazingFeature`)
3. Faça o Commit das suas Alterações (`git commit -m 'Add AmazingFeature'`)
4. Faça o Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request




<!-- LICENSE -->
## License

Distributed under the Apache 2.0 License. See `LICENSE` for more information.




<!-- CONTACT -->
## Contato

LEDS - [@ledsifes](https://www.instagram.com/ledsifes/) - leds@ifes.edu.br

Projeto: [github.com/LEDS/MiteHunter](https://github.com/LEDS/MiteHunter/tree/main)




<!-- ACKNOWLEDGMENTS -->
## Agradecimentos

* [Prof. Dr. Fidelis Zanetti de Castro](https://www.linkedin.com/in/fidelis-zanetti-de-castro-1bab66247/?originalSubdomain=br) - Que supervisionou de perto o desenvolvimento da rede neural neste projeto. Seus insights e orientações foram inestimáveis, proporcionando uma base sólida para o progresso e conclusão deste trabalho.
* [Prof. Dr. Victorio Albani de Carvalho
](http://lattes.cnpq.br/6035323365313300) - Que acompanhou de perto o desenvolvimento da aplicação. Sua experiência e apoio incansável foram elementos-chave para o sucesso deste projeto.
* [Laboratório de Extensão em Desenvolvimento de Soluções](https://www.exemplo.com/laboratorio) - Agradecemos a toda a equipe do laboratório pela oportunidade de participação, ambiente colaborativo, estrutura e conhecimento que viabilizaram o desenvolvimento do projeto. 


<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[Budibase.js]: https://camo.githubusercontent.com/91cabd49291e9be02853d7841cb674c80ddd86b3c6ebc8bca2b471c4f115c656/68747470733a2f2f696d672e736869656c64732e696f2f7374617469632f76313f7374796c653d666f722d7468652d6261646765266d6573736167653d427564696261736526636f6c6f723d303030303030266c6f676f3d4275646962617365266c6f676f436f6c6f723d464646464646266c6162656c3d
[Budibase-url]: https://budibase.com/
[Python-url]: https://www.python.org/
[Python.js]: https://camo.githubusercontent.com/83f28bdf9b2f1bac2f94c51c1fd1e2bcc290c4c35101c813c0a94e3e5fd2acdb/68747470733a2f2f696d672e736869656c64732e696f2f7374617469632f76313f7374796c653d666f722d7468652d6261646765266d6573736167653d507974686f6e26636f6c6f723d333737364142266c6f676f3d507974686f6e266c6f676f436f6c6f723d464646464646266c6162656c3d
[Django-url]: https://www.djangoproject.com/
[Django.js]: https://img.shields.io/static/v1?style=for-the-badge&message=Django&color=092E20&logo=Django&logoColor=FFFFFF&label=
[Docker-url]: https://www.docker.com/
[Docker.js]: https://img.shields.io/static/v1?style=for-the-badge&message=Docker&color=2496ED&logo=Docker&logoColor=FFFFFF&label=

[contributors-shield]: https://img.shields.io/github/contributors/LEDS/MiteHunter.svg?style=for-the-badge
[contributors-url]: https://github.com/LEDS/MiteHunter/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/LEDS/MiteHunter.svg?style=for-the-badge
[forks-url]: https://github.com/LEDS/MiteHunter/network/members
[stars-shield]: https://img.shields.io/github/stars/LEDS/MiteHunter.svg?style=for-the-badge
[stars-url]: https://github.com/LEDS/MiteHunter/stargazers
[issues-shield]: https://img.shields.io/github/issues/LEDS/MiteHunter.svg?style=for-the-badge
[issues-url]: https://github.com/LEDS/MiteHunter/issues
[license-shield]: https://img.shields.io/github/license/LEDS/MiteHunter.svg?style=for-the-badge
[license-url]: https://github.com/LEDS/MiteHunter/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/school/ledsifes/mycompany/verification/
[product-screenshot]: infra/Fotos/ExemploBudibase.png