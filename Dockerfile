FROM python:3.8-slim

WORKDIR /gourmet

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . .

ENTRYPOINT ["sh", "boot.sh" ]