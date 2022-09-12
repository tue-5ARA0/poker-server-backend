FROM python:3.9

# Install base utilities
RUN apt-get update
RUN apt-get install -y wget && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY environment_linux.yml /code/environment_linux.yml
COPY requirements_linux.txt /code/requirements_linux.txt

ENV CONDA_DIR /opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda

ENV PATH=$CONDA_DIR/bin:$PATH

RUN conda init bash
RUN conda config --set remote_read_timeout_secs 1200.0
RUN conda env create -f environment_linux.yml
RUN conda activate pokerbot39

RUN pip install --only-binary grpcio,grpcio-tools,matplotlib,protobuf -r requirements_linux.txt
RUN pip install psycopg2

COPY . /code/

RUN python init.py