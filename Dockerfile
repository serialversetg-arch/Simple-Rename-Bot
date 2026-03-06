FROM python:3.10-slim-buster

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y git python3-pip ffmpeg

WORKDIR /app
COPY . /app/

RUN pip3 install --no-cache-dir -r requirements.txt

# Health Check Port
EXPOSE 8000

CMD ["python3", "bot.py"]



