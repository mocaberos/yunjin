FROM python:3.10-slim-bullseye

LABEL service="yunjin"

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y --no-install-recommends git gcc g++
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN python3 -m pip install -r ./requirements.txt

COPY . /app

EXPOSE 1190
ENTRYPOINT ["/app/docker/scripts/docker-entrypoint.sh"]
CMD ["python3", "-m", "uvicorn", "--log-level", "info", "--host", "0.0.0.0", "--port", "1190", "main:app"]
