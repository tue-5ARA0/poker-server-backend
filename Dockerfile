FROM --platform=linux/amd64 python:3.10.22-slim-bookworm

WORKDIR /code

# Set the PYTHONPATH environment variable
ENV PYTHONPATH="/code"

# Set SHELL to bash with pipefail option as we use pipes in our scripts
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Build dependencies
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        wget=1.21.3-1+deb12u1 \
        gnupg=2.2.40-1.1+deb12u2 \
        curl=7.88.1-10+deb12u15 \
        build-essential=12.9 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install poetry package manager
RUN python3 -m pip install --no-cache-dir poetry==1.8.2 \
    && poetry config virtualenvs.create false

# Postgres client (these pinned versions are provided by Debian itself)
RUN apt-get update \
    && apt-get install --no-install-recommends -y postgresql-client-15=15.19-0+deb12u1 \
                                                  libpq-dev=15.19-0+deb12u1 \
                                                  libpq5=15.19-0+deb12u1 \
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
