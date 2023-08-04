## YouTube Downloader API using FastAPI and yt-dlp

This project demonstrates how to build a simple API using `FastAPI` and the `yt-dlp` library to download YouTube music audios. The API exposes endpoints that allow users to submit YouTube video URLs and download the audio in m4a format. This project is built as microservice for my [`music-dl-server`](https://github.com/nil1729/music-dl-server) project.

### Features
- It exposes an API which accept a YouTube URL and download the audio and saved it in a desired location. You can view the original project to understand its workings.


### Prerequisites
To run this project, you need the following dependencies installed on your system:
- Python 3.7+
- FFmpeg


### Standalone Installation Guide
1. Clone the repository
   ```shell
    git clone https://github.com/nil1729/yt-dl-fast-api.git
   ```
2. Create a virtual environment
   ```shell
    python3 -m venv venv
    source venv/bin/activate
   ```
3. Install the dependencies
   ```shell
    pip3 install -r requirements.txt
   ```
4. Set Environment Variables
   ```shell
    export DOWNLOAD_PATH="/path/to/downloads/directory"
    export PORT=9090
    export FFMPEG_LOCATION="ffmpeg/bin/path"
   ```
5. Start the FastAPI server:
   ```shell
    uvicorn main:app --host 0.0.0.0 --port $PORT
   ```

### Docker Installation Guide
1. Build the docker image
   ```shell
    docker build -t yt-dl-fast-api-server .
   ```
2. Run the application
   ```shell
    docker run \
          --name yt-dl-fast-api-server \
          -p 9090:80 \
          -v $(pwd)/downloads:/usr/downloads \
          -d yt-dl-fast-api-server
   ```
3. Check the Logs
   ```shell
    docker logs yt-dl-fast-api-server -f
   ```

### API(s)
- **Health Check**: GET `/`
- **Swagger Documentation**: GET `/docs`

### Acknowledgments
- [FastAPI](https://fastapi.tiangolo.com/) - FastAPI documentation and examples.
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - yt-dlp GitHub repository.
