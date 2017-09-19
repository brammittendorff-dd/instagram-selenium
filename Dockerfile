FROM python:3.6
RUN mkdir /app
RUN mkdir /config
COPY ./requirements.txt /config/
RUN pip install -r /config/requirements.txt
WORKDIR /app
COPY ./app/ /app/