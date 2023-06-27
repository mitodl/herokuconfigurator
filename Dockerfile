FROM python:3.11-alpine
ENV PYTHONUNBUFFERED=1

WORKDIR /opt/resource
CMD ["/bin/sh"]

COPY bin/* /opt/resource/
COPY lib/* /opt/resource/lib/


