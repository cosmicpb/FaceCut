FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN apt update \
    && apt install -y \
        ffmpeg \
        git \
        libsm6 \
        libxext6 \
        python3-requests \
    && pip install -r requirements.txt \ 
    && pip install requests

CMD ["python", "main.py"]
