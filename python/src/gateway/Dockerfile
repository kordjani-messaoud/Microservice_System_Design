# syntax=docker/dockerfile:1.7-labs
FROM python:3.9.20-bullseye

RUN <<EOF
apt-get update
apt-get install -y --no-install-recommends --no-install-suggests build-essential default-libmysqlclient-dev
pip install --no-cache-dir --upgrade pip
EOF

WORKDIR /app

COPY --exclude=venv/ --exclude=manifests/ . /app

RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 8080

CMD ["python", "server.py"]