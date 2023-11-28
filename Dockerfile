FROM python:latest

WORKDIR /usr/src/app
COPY . .

RUN pip install pytest

CMD ["bash", "-c", "while true; do sleep 3600; done"]