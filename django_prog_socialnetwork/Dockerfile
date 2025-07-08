FROM python:3.11.3-alpine

WORKDIR /django_prog_socialnetwork

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apk update \
    && apk add --no-cache postgresql-dev gcc python3-dev musl-dev libffi-dev

RUN mkdir /django_prog_socialnetwork/media /django_prog_socialnetwork/static

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "django_prog_socialnetwork.wsgi:application", "--bind", "0.0.0.0:8000"]