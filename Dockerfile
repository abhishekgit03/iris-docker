FROM python:3.9.1
COPY . /usr/app/
EXPOSE $PORT
WORKDIR /usr/app/
RUN pip install -r requirements.txt
CMD gunicorn --workers=4 0.0.0.0:$PORT app:app