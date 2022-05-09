FROM python:slim

RUN useradd microservicios

WORKDIR /home/siguiente_letra

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY boot.sh config.py listado_de_palabras_sin_tildes.txt siguiente_letra.py siguiente-letra-flask.py ./
RUN chmod +x boot.sh

ENV FLASK_APP siguiente-letra-flask

RUN chown -R microservicios:microservicios ./
USER microservicios

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]