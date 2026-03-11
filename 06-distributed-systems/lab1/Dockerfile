FROM python:3.15.0a7-alpine3.22
WORKDIR /app
COPY requirements.txt .
RUN pip install --break-system-packages -r requirements.txt
COPY start.sh .
CMD [ "/app/start.sh" ]
