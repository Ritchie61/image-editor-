FROM python:3.9
WORKDIR /app
COPY app.py requirements.txt ./
RUN apt-get update && apt-get install -y tesseract-ocr
RUN pip install -r requirements.txt
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8002"]
