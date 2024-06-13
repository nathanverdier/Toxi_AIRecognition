from python:latest

WORKDIR /app

EXPOSE 80

COPY codeAI /app
COPY getToken.py /app
COPY getImagesApi.py /app
COPY requirements.txt /app
COPY start.sh /app

RUN pip install --upgrade pip && \
    apt-get update && \
    apt-get install -y libgl1-mesa-glx cmake build-essential libopencv-dev libopenblas-dev liblapack-dev libx11-dev libgtk-3-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install gunicorn

RUN chmod +x /app/start.sh

ENTRYPOINT ["/app/start.sh"]