FROM python:3.9

ADD twitter_bot.py .
COPY config.py .
COPY credentials.py .
COPY requirements.txt .

RUN pip install -r requirements.txt



CMD ["python", "./twitter_bot.py"]