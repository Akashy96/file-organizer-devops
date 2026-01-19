FROM python:3.11-slim

WORKDIR /app

COPY src/ /app/src/

CMD ["python", "/app/src/organizer.py"]