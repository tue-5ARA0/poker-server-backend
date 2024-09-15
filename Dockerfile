FROM --platform=linux/amd64 python:3.10.10-slim-buster

WORKDIR /code

# Set the PYTHONPATH environment variable
ENV PYTHONPATH="/code:${PYTHONPATH}"

# Set SHELL to bash with pipefail option as we use pipes in our scripts
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Build dependencies
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        wget=1.20.1-1.1 \
        gnupg=2.2.12-1+deb10u2 \
        curl=7.64.0-4+deb10u9 \
        build-essential=12.6 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install poetry package manager
RUN python3 -m pip install --no-cache-dir poetry==1.8.2 \
    && poetry config virtualenvs.create false

# Postgres client
RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt buster-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
RUN curl --silent https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        postgresql-client-12=12.20-1.pgdg100+1 \
        libpq-dev=16.4-1.pgdg100+1 \
        ffmpeg=7:4.1.11-0+deb10u1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock ./

RUN --mount=type=cache,target=/root/.cache/pypoetry/cache \
    --mount=type=cache,target=/root/.cache/pypoetry/artifacts \
    poetry install --no-interaction --no-ansi

# Copy the entire app to the working directory
COPY . ./

# Ensure __init__.py files are present
RUN touch proto/__init__.py

# Regenerate protobuf files
RUN poetry run python -m grpc_tools.protoc \
    -I./proto \
    --python_out=. \
    --grpc_python_out=. \
    ./proto/game/*.proto

# Install the project itself
RUN poetry install --only-root
