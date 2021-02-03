FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
COPY . /code
RUN python3 manage.py makemigrations \
    && python3 manage.py migrate

EXPOSE 8000
CMD python3 manage.py runserver 0.0.0.0:8000