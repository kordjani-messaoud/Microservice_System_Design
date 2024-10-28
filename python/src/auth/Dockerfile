# syntax=docker/dockerfile:1


# Base image
# Every build instruction below is an image layer
FROM python:3.9.20-bullseye 

# Run bash command inside the base image
# Update c compiler 'cbuild-essential' and sql client with minimal space comsubtion
# Apparently pip can upgrade it self 
RUN apt-get update\
    && apt-get install -y --no-install-recommends --no-install-suggests\
        build-essential default-libmysqlclient-dev\
            && pip install --no-cache-dir --upgrade pip


# Make directory app
WORKDIR /app
# Copy from the working directory (at image buiding time) to the container directory /app
COPY ./requirements.txt /app

# Install python dependencies from requirements file 
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY . /app

# Image listening at port 5000
EXPOSE 5000

# Set the command that is run when the container based on this image is starts
# Start the Python applicatiuon
#CMD ["python", "server.py"]
CMD python server.py


