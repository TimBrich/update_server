FROM python:3.7
MAINTAINER Brychikov Daneel <brychdaneel@gmail.com>

#RUN useradd -ms /bin/false esp_update_server
WORKDIR /home/esp_update_server

COPY images/esp_update_server/requirements.txt requirements.txt

RUN pip3 install -r requirements.txt &&\
    rm requirements.txt

COPY images/esp_update_server/startup.sh startup.sh
COPY images/esp_update_server/init.sh init.sh  

#USER esp_update_server
WORKDIR /home/esp_update_server/src
