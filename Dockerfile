FROM python:3.11-slim

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app

COPY src/ /app

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
