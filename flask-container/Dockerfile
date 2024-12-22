FROM python:3.9-slim-bullseye

WORKDIR /app

COPY app.py /app/
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 52039

CMD ["flask", "run", "--host=0.0.0.0"]