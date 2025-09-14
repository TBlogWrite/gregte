FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .
COPY number_lucky.csv .

CMD ["python", "app.py"]
