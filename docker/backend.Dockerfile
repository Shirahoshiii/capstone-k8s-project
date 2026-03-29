FROM nginx:alpine
COPY app/frontend /usr/share/nginx/html

FROM python:3.10

WORKDIR /app

COPY app/backend .

RUN pip install fastapi uvicorn

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]