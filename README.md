<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/FagundesMatheus/MICROSSERVICO-ESTOQUE">
  </a>

<h3 align="center">Microsserviço de Estoque</h3>

  <p align="center">
    Microsserviço de estoque utilizando Python com FastAPI e PostgreSQL
    <br />
    <a href="https://fagundesmatheus.github.io/MICROSSERVICO-ESTOQUE/"><strong>Veja a documentação »</strong></a>
    <br />
    <br />
    <!-- <a href="https://github.com/FagundesMatheus/MICROSSERVICO-ESTOQUE">View Demo</a>
    &middot;
    <a href="https://github.com/FagundesMatheus/MICROSSERVICO-ESTOQUE/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/FagundesMatheus/MICROSSERVICO-ESTOQUE/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
-->
</p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Sumário</summary>
  <ol>
    <li>
      <a href="#sobre-o-projeto">Sobre o Projeto</a>
      <ul>
        <li><a href="#tecnologias-utilizadas">Tecnologias Utilizadas</a></li>
      </ul>
    </li>
    <li>
      <a href="#primeiros-passos">Primeiros passos</a>
      <ul>
        <li><a href="#pr%C3%A9-requisitos">Pré-requisitos</a></li>
        <li><a href="#instala%C3%A7%C3%A3o">Instalação</a></li>
      </ul>
    </li>
    <li><a href="#uso">Uso</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#licen%C3%A7a">Licença</a></li>
    <li><a href="#contato">Contato</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Sobre o Projeto


Este projeto implementa uma solução de controle de estoque baseada em arquitetura de microsserviços. 
Essa abordagem permite encapsular a lógica de negócio de forma independente, possibilitando que o serviço seja reutilizado por outras aplicações sem dependências externas diretas.
<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Tecnologias Utilizadas

* [![Python][Python]][Python-url]
* [![FastAPI][FastAPI]][FastAPI-url]
* [![SQLAlchemy][SQLAlchemy]][SQLAlchemy-url]
* [![PostgreSQL][PostgreSQL]][PostgreSQL-url]
* [![Gunicorn][Gunicorn]][Gunicorn-url]
* [![Poetry][Poetry]][Poetry-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- Primeiros passos -->
## Primeiros passos

Esse é um exemplo de como rodar a aplicação localmente via docker compose.

### Pré-requisitos

Este projeto utiliza Docker e Docker Compose para rodar. Certifique-se de ter os seguintes programas instalados:

* **Docker** 26.1.1 ou superior
  ```sh
  docker --version
  ```
* **Docker Compose** v2.27.0 ou superior
  ```sh
  docker compose version
  ```

### Instalação

1. Clone o repositório
   ```sh
   git clone https://github.com/FagundesMatheus/MICROSSERVICO-ESTOQUE.git
   cd estoque-service
   ```

2. Crie o arquivo `.env` baseado no template fornecido
   ```sh
   cp .env.template .env
   ```
   Edite o `.env` com as credenciais desejadas.

3. Inicie o serviço com Docker Compose
   ```sh
   docker compose up --build
   ```

   Esse comando irá:
   - Construir a imagem Docker da aplicação
   - Inicializar o banco de dados PostgreSQL
   - Rodar as migrações iniciais
   - Iniciar o serviço na porta `5001`

4. Acesse a aplicação
   ```
   http://localhost:5001
   ```

   A documentação interativa da API estará disponível em:
   ```
   http://localhost:5001/docs
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- Usagem EXAMPLES -->
## Uso

A API oferece endpoints para gerenciar produtos, estoque e reservas. Exemplos de uso:

### Listar todos os produtos
```bash
curl http://localhost:5001/produtos
```

### Consultar estoque de um produto
```bash
curl http://localhost:5001/estoque/{id}
```

### Criar um novo produto
```bash
curl -X POST http://localhost:5001/produto \
  -H "Content-Type: application/json" \
  -d '{"nome": "Produto Teste", "descricao": "Descrição", "quantidade": 100}'
```

### Adicionar estoque
```bash
curl -X POST http://localhost:5001/estoque/adicionar \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "quantidade": 50}'
```

### Criar uma reserva
```bash
curl -X POST http://localhost:5001/reserva \
  -H "Content-Type: application/json" \
  -d '{"idproduto": 1, "idpedido": 123, "quantidade": 10}'
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Implementar eventos Kafka
- [ ] Implementar histórico de movimentações de estoque
- [ ] Adicionar suporte para variações de produtos (tamanho, cor, etc.)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- LICENSE -->
## Licença

Distribuído sob a Licença MIT. Veja `LICENSE` para mais informações.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contato

Matheus Fagundes - matheus.fagundes0424@gmail.com

Project Link: [https://github.com/FagundesMatheus/MICROSSERVICO-ESTOQUE](https://github.com/FagundesMatheus/MICROSSERVICO-ESTOQUE)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/FagundesMatheus/MICROSSERVICO-ESTOQUE.svg?style=for-the-badge
[contributors-url]: https://github.com/FagundesMatheus/MICROSSERVICO-ESTOQUE/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/FagundesMatheus/MICROSSERVICO-ESTOQUE.svg?style=for-the-badge
[forks-url]: https://github.com/FagundesMatheus/MICROSSERVICO-ESTOQUE/network/members
[stars-shield]: https://img.shields.io/github/stars/FagundesMatheus/MICROSSERVICO-ESTOQUE.svg?style=for-the-badge
[stars-url]: https://github.com/FagundesMatheus/MICROSSERVICO-ESTOQUE/stargazers
[issues-shield]: https://img.shields.io/github/issues/FagundesMatheus/MICROSSERVICO-ESTOQUE.svg?style=for-the-badge
[issues-url]: https://github.com/FagundesMatheus/MICROSSERVICO-ESTOQUE/issues
[license-shield]: https://img.shields.io/github/license/FagundesMatheus/MICROSSERVICO-ESTOQUE.svg?style=for-the-badge
[license-url]: https://github.com/FagundesMatheus/MICROSSERVICO-ESTOQUE/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
<!-- Shields.io badges. You can a comprehensive list with many more badges at: https://github.com/inttter/md-badges -->
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 

[FastAPI]: https://img.shields.io/badge/FastAPI-3776AB?style=for-the-badge&logo=fastapi&logoColor=white
[FastAPI-url]: https://fastapi.tiangolo.com/
[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Flask]: https://img.shields.io/badge/Flask-3776AB?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/
[SQLAlchemy]: https://img.shields.io/badge/SQLAlchemy-3776AB?style=for-the-badge&logo=sqlalchemy&logoColor=white
[SQLAlchemy-url]: https://www.sqlalchemy.org/
[PostgreSQL]: https://img.shields.io/badge/PostgreSQL-3776AB?style=for-the-badge&logo=postgresql&logoColor=white
[PostgreSQL-url]: https://www.postgresql.org/
[Gunicorn]: https://img.shields.io/badge/Gunicorn-3776AB?style=for-the-badge&logo=gunicorn&logoColor=white
[Gunicorn-url]: https://gunicorn.org/
[Poetry]: https://img.shields.io/badge/Poetry-3776AB?style=for-the-badge&logo=poetry&logoColor=white
[Poetry-url]: https://python-poetry.org/