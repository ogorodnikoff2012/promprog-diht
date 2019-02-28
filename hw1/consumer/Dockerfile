FROM python:3.6-alpine
ADD requirements.txt /code/requirements.txt
WORKDIR /code
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps
ADD consumer.py /code/consumer.py

CMD ["python", "-u", "/code/consumer.py"]
