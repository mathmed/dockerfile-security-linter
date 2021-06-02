FROM socrata/java8

EXPOSE 6010
EXPOSE 6012
ENV JMX_PORT 6019
EXPOSE 6019

ENV SERVER_ROOT /srv/soda-fountain/
# TODO sbt task to copy latest jar into docker/
ENV SERVER_ARTIFACT soda-fountain-jetty-assembly.jar
ENV SERVER_CONFIG soda-fountain.conf

# defaults
ENV BALBOA_ACTIVEMQ_URI not-configured
ENV BALBOA_JMS_QUEUE not-configured
ENV ENABLE_GRAPHITE false
ENV GRAPHITE_HOST 0.0.0.0
ENV GRAPHITE_PORT 0
ENV JAVA_XMX 512m
ENV JAVA_MAX_METASPACE 64m
ENV LOG_METRICS false
ENV SODA_FOUNTAIN_DB_NAME metasoda
ENV SODA_FOUNTAIN_DB_PORT 5432
ENV SODA_FOUNTAIN_DB_USER soda_fountain
ENV SPANDEX_PORT 80

WORKDIR $SERVER_ROOT

COPY ship.d /etc/ship.d
COPY ${SERVER_CONFIG}.j2 $SERVER_ROOT/
COPY $SERVER_ARTIFACT $SERVER_ROOT/


# Comentário por Mateus Medeiros
# SM08 linha 1
# SM04 linha 17
# SM03 linha 24
# SM05 linha 9