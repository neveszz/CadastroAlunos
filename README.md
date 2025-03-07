# Sistema de Cadastro de Alunos

Este projeto é um sistema de cadastro de alunos com autenticação, desenvolvido utilizando **Django**.

## Tecnologias Utilizadas
- Django
- SQLite (Banco de Dados padrão do Django)
- TailwindCSS (opcional para estilização)

## Funcionalidades
- Cadastro de usuários
- Autenticação de usuários (Login e Logout)
- Cadastro de alunos
- Listagem de alunos cadastrados
- Edição de dados dos alunos
- Exclusão de alunos

## Pré-requisitos
- Python 3.x
- Virtualenv (opcional)

## Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Crie o ambiente virtual e ative:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate    # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Realize as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```

5. Crie um superusuário para acessar a área administrativa:
   ```bash
   python manage.py createsuperuser
   ```

6. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

A aplicação estará disponível em: `http://localhost:8000`

## Como Usar
1. Acesse a página de login e autentique-se.
2. Utilize o sistema para cadastrar, listar, editar e excluir alunos.
3. Acesse o painel administrativo em `/admin` para ter controle total sobre os dados.

