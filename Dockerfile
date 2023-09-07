FROM python:3-alpine
WORKDIR /usr/src/appIMC
EXPOSE 80
COPY requirements.txt .
RUN pip install -qr requirements.txt
COPY . .
CMD [ "python", "./main.py" ]
