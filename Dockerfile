FROM python:3.11.0
WORKDIR /app
ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    FLASK_APP=src.app.app \
    FLASK_RUN_HOST=0.0.0.0
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    curl \
    build-essential 

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD [ "flask", "run" ]