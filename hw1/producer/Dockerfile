FROM python:3.6-alpine
ADD requirements.txt /code/requirements.txt
WORKDIR /code
RUN python3 -m pip install -r requirements.txt --no-cache-dir
ADD producer.py /code/producer.py

CMD ["python", "-u", "/code/producer.py"]
