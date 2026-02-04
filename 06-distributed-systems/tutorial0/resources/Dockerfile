FROM python:3.11-alpine3.23

LABEL description="Simple file uploader image"

WORKDIR /app

COPY ./file-uploader.py /app/

#RUN pip install flask && chmod +x /app/file-uploader.py

EXPOSE 5000

CMD [ "/app/file-uploader.py", "0.0.0.0", "--port", "5000" ]
