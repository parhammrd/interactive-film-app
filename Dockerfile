# Use an official Python runtime as the base image
FROM python:3.9.18-slim-bullseye

# Install system dependencies
RUN apt-get update && apt-get upgrade

# Set the working directory inside the container
WORKDIR /interactive-film-api

# Copy project files into the container
COPY . /interactive-film-api/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# ENTRYPOINT [ "executable" ]