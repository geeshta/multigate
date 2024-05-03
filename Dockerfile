FROM python:3.12-slim-bullseye

RUN apt update \
    && apt install -y --no-install-recommends curl build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://deb.nodesource.com/setup_21.x | bash -

RUN apt install -y nodejs
RUN npm i -g yarn

WORKDIR /app

COPY .env .

# Install Python project
COPY server/ /app/server
COPY requirements.lock .
RUN PYTHONDONTWRITEBYTECODE=1 pip install --no-cache-dir -r requirements.lock

# Install Node project
COPY frontend/ /app/frontend
COPY yarn.lock .
COPY package.json .
COPY vite.config.ts .
RUN yarn

COPY Makefile .
EXPOSE 8300
EXPOSE 5300
ENTRYPOINT [ "make", "serve_docker"  ]
