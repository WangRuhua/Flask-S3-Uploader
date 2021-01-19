FROM ubuntu:20.10


LABEL maintaner="Ruhua Wang"

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev

COPY ./requirements.txt /app/requirements.txt
COPY ./version.txt /app/version.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

#ENTRYPOINT [ "python" ]

CMD [ "flask", "run","--host=0.0.0.0","--port=80"]
