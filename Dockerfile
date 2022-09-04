FROM python:3.10

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY server.py .
COPY my_constants.py .
COPY project project
ENV FLASK_APP=server.py

CMD gunicorn run:app -b 0.0.0.0:25000