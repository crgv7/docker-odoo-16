FROM odoo:17.0

LABEL MAINTAINER Marlon Falcon <mfalconsoft@gmail.com>
USER root

RUN pip3 install dropbox
