from python:latest

WORKDIR /app

EXPOSE 80

COPY codeAI /app
COPY getToken.py /app
COPY getImagesApi.py /app
COPY requirements.txt /app

RUN pip install --upgrade pip

RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx

RUN apt-get update && \
    apt-get install -y cmake build-essential libopencv-dev libopenblas-dev liblapack-dev libx11-dev libgtk-3-dev

RUN pip install --no-cache-dir -r requirements.txt

RUN python3 getImagesApi.py

CMD [ "gunicorn", "-w", "4", "-b", "0.0.0.0:80", "mainAI:app" ]
