FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /code

COPY . /code

WORKDIR /code

RUN pip install -r requirements.txt

RUN [ "python", "-c", "import nltk; nltk.download('all')" ]

ENTRYPOINT python manage.py runserver "0.0.0.0:8000"
EXPOSE 8000


  