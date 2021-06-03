FROM openjdk:8

MAINTAINER delivery-engineering@netflix.com

COPY . workdir/

WORKDIR workdir

RUN GRADLE_USER_HOME=cache ./gradlew -I gradle/init-publish.gradle buildDeb -x test && \
  dpkg -i ./kayenta-web/build/distributions/*.deb && \
  cd .. && \
  rm -rf workdir

CMD ["/opt/kayenta/bin/kayenta"]


# Comentário por Mateus Medeiros
# SM03 linha 9
# SM01