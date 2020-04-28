FROM python:3.7-slim

COPY . /app
WORKDIR /app

RUN apt-get update
RUN apt-get install -y build-essential libpq-dev

RUN pip install -r requirements.txt

EXPOSE 5000

# ENTRYPOINT ["python"]
# CMD ["run.py"]

CMD [ "uwsgi", "--ini", "app.ini" ]
