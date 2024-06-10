from python:latest

WORKDIR /app

EXPOSE 80

COPY codeAI /app
COPY getImagesApi.py /app
COPY requirements.txt /app

RUN pip install --upgrade pip

RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx

RUN apt-get update && \
    apt-get install -y cmake build-essential libopencv-dev libopenblas-dev liblapack-dev libx11-dev libgtk-3-dev

RUN pip install -r requirements.txt

RUN python3 getImagesApi.py

CMD ["python3", "mainAI.py"]
