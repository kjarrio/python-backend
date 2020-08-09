FROM python:3
ENV PYTHONUNBUFFERED 1

# Dockerize - para rodar apenas quando banco de dados estiver pronto
ENV DOCKERIZE_VERSION v0.6.1
RUN wget -q https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN mkdir /app
WORKDIR /app

# Instalar dependencias do Python
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/
