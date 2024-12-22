FROM python:3.9-slim-bullseye

WORKDIR /ml

COPY model.py /ml/
COPY requirements.txt /ml/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "model.py"]