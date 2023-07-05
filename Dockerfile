# Use a Python base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /usr/app

# Copy the requirements file to the container
COPY requirements.txt .

# Install FFmpeg
RUN apt-get update && apt-get install -y ffmpeg

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI app code to the container
COPY main.py /usr/app

ENV PORT 80
ENV DOWNLOAD_PATH /usr/downloads
ENV FFMPEG_LOCATION /usr/bin/ffmpeg

# Expose the port on which the FastAPI app will run
EXPOSE $PORT

# Set the command to run the FastAPI app when the container starts
ENTRYPOINT uvicorn main:app --host 0.0.0.0 --port $PORT
