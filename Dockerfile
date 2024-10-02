FROM --platform=linux/amd64 python:3.10.10-slim-bullseye

WORKDIR /code

# Set the PYTHONPATH environment variable
ENV PYTHONPATH="/code:${PYTHONPATH}"

# Set SHELL to bash with pipefail option as we use pipes in our scripts
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Build dependencies
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        wget=1.21-1+deb11u1 \
        gnupg=2.2.27-2+deb11u2 \
        curl=7.74.0-1.3+deb11u13 \
        build-essential=12.9 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install poetry package manager
RUN python3 -m pip install --no-cache-dir poetry==1.8.2 \
    && poetry config virtualenvs.create false

# Postgres client
RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt bullseye-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
RUN curl --silent https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN apt-get update \
    && apt-get install --no-install-recommends -y postgresql-client-13=13.16-0+deb11u1 \
                                                  libpq-dev=13.16-0+deb11u1 \
                                                  libpq5=13.16-0+deb11u1 \
                                                  ffmpeg=7:4.3.7-0+deb11u1 \
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

# Regenerate protofiles
RUN poetry run python -m grpc_tools.protoc \
    -I./proto \
    --python_out=. \
    --grpc_python_out=. \
    ./proto/game/*.proto

# Install the project itself
RUN poetry install --only-root
