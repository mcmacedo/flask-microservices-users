FROM python:3.6.1

# Define o diretório de trabalho
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Adiciona o arquivo de dependências e as instala
ADD ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# Adiciona a aplicação ao diretório de trabalho
ADD . /usr/src/app

# Inicia o servidor
CMD python manage.py runserver -h 0.0.0.0
