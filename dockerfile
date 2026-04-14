FROM python:3.11-slim

RUN apt-get update && apt-get install -y git gcc && rm -rf /var/lib/apt/lists/*

WORKDIR /app
RUN git clone https://github.com/budget_tracker && \
    git checkout 34854a03f3bcddc3c4099f2feb87a4359a37d281

    
WORKDIR /app
