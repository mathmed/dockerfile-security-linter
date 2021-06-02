FROM postgres:9.5.1
MAINTAINER altfatterz@gmail.com
ENV POSTGRES_USER docker
ENV POSTGRES_DB mydb
COPY 1_schema.sql /docker-entrypoint-initdb.d/
COPY 2_data.sql /docker-entrypoint-initdb.d/


# Comentário por Mateus Medeiros
# SM03 linha 3
