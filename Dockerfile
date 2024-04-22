FROM python:3.9
WORKDIR /app
COPY randomparagraphs.py .
ENTRYPOINT ["python", "randomparagraphs.py"]