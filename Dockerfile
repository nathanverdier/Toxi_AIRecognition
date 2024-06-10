from python:latest

WORKDIR /app

COPY codeAI /app

RUN pip install --upgrade pip

RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx

RUN apt-get update && \
    apt-get install -y cmake build-essential libopencv-dev libopenblas-dev liblapack-dev libx11-dev libgtk-3-dev

RUN pip install -r requirements.txt

EXPOSE 80

RUN python3 getImages.py

CMD ["python3", "mainAI.py"]
