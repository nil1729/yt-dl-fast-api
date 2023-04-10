import os
import random
import yt_dlp
import time
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

download_path = os.environ.get('DOWNLOAD_PATH')

if download_path is None:
    raise Exception('application environment not set properly')


class YtVideoDownloadRequestBody(BaseModel):
    url: str


def generate_random_file_name():
    timestamp_ms = int(time.time() * 1000)
    random_number = random.random()
    return f"{timestamp_ms}{random_number}"


app = FastAPI()


@app.post("/api/download")
def download_video(body: YtVideoDownloadRequestBody):
    file_name = f'{generate_random_file_name()}.m4a'
    urls = [body.url]
    ydl_opts = {
        'outtmpl': {
            'default': "/".join([download_path, file_name]),
        },
        'format': 'm4a/bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(urls)

    if error_code == 0:
        return {"status": "success", "file_name": file_name}
    else:
        raise HTTPException(506, detail="download failed for internal server error")
