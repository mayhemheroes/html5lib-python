FROM python:3.11-slim

RUN apt-get update && apt-get install -y clang && rm -rf /var/lib/apt/lists/*
RUN pip3 install atheris

COPY . /html5lib
WORKDIR /html5lib
RUN python3 -m pip install -r requirements.txt
RUN python3 -m pip install . && chmod +x fuzz/fuzz_html_parser.py
