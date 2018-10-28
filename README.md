## Executando Tarefas assíncronas no Django usando Celery

Código fonte do exemplo utilizado na palestra *"Executando Tarefas assíncronas no Django usando Celery"* ministrada na **Python Brasil[14]** no dia 21 de outubro de 2018 na cidade de Natal no Rio Grande do Norte.

No exemplo eu utilizo celery para processar de forma assíncrona a criação de usuarios em massa através de um arquivo *.csv*.

Link dos slides [aqui](https://speakerdeck.com/werberth/executando-tarefas-assincronas-no-django-usando-celery).

## Instalação
```
    # Criando ambiente virtual
    python -m venv nome-do-ambiente-virtual
    source nome-do-ambiente-virtual/bin/activate

    # Clonando o projeto
    git clone https://github.com/werberth/python-brasil-14-django-celery-talk.git

    # Entrando na pasta e instalando as dependências
    cd python-brasil-14-django-celery-talk
    pip install -r requirements.txt
    
    # rodando as migrações e executando o projeto
    python manage.py migrate
    python manage.py runserver
```
