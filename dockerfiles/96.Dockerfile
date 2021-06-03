FROM docker.elastic.co/kibana/kibana-oss:6.4.1

ENV ELASTICSEARCH_URL=http://jhipster-elasticsearch:9200

COPY kibana.yml /usr/share/kibana/config/kibana.yml
RUN ./bin/kibana-plugin install https://github.com/sivasamyk/logtrail/releases/download/v0.1.30/logtrail-6.4.1-0.1.30.zip
COPY logtrail.json /usr/share/kibana/plugins/logtrail/logtrail.json

# Comentário por Mateus Medeiros
# SM09 linha 1
# SM06 linha 3
# SM01