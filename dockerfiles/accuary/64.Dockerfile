FROM aist-tensorflow

USER root

COPY requirements.txt /app/

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

COPY supervisord.conf /etc/supervisord.conf

ENTRYPOINT ["supervisord", "--nodaemon", "--configuration", "/etc/supervisord.conf"]

# Comentário por Mateus Medeiros
# SM09 linha 1
# SM01 linha 3
# SM01