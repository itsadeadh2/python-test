from python:3.6.6

workdir /app

copy . .

cmd python test.py