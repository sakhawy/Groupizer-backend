FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /groupizer_backend/
COPY ./requirements.txt /groupizer_backend/
RUN pip install -r requirements.txt

COPY . /groupizer_backend/