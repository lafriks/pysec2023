FROM mcr.microsoft.com/vscode/devcontainers/python:3-bullseye

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y python3.9 python3-venv \
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*
