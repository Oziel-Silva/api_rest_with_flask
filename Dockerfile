FROM python:3.8

WORKDIR /code
 

# Install python requirements to run application.
COPY requirements.txt /code
RUN python3 -m pip install -r requirements.txt

COPY . /code