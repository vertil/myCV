FROM animcogn/face_recognition:latest

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y


COPY requirements.txt requirements.txt

RUN pip3 install -r ./requirements.txt

#COPY images images


COPY main.py main.py

CMD [ "python3", "main.py" ]
