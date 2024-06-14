# Prova 2 - Módulo 10

Desenvolvido por Lyorrei Shono Quintão

## Introdução

Este projeto é uma API simples desenvolvida para a prova 2 do módulo 10. Implementa uma API RESTful assíncrona usando Fastapi em Python e inclui um CRUD de blogs.

## Configuração e Instalação

Antes de tudo, clone o repositório:
```bash
git clone git@github.com:lyorrei-inteli/prova2_mod10.git
cd prova2_mod10
```

Depois, navegue até a root do repositório e siga os passos a seguir dependendo se deseja rodar localmente ou via Docker:

### Localmente
1. Crie o ambiente virtual:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute a aplicação:
   ```bash
   fastapi dev main.py
   ```

   A aplicação estará disponível em `http://127.0.0.1:8000/`.

### Docker
1. Rode o container docker:
   ```bash
   docker compose up
   ```

A aplicação estará disponível em `http://127.0.0.1/`.

## Insomnia

Você pode utilizar o arquivo `insomnia.yaml` para importar as requisições no Insomnia e testá-las.
