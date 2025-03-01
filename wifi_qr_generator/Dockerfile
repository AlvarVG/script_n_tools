FROM python:3.13.2-alpine

COPY qr_generator.py requirements.txt /code/

RUN pip install --no-cache-dir -r /code/requirements.txt

WORKDIR /app

ENTRYPOINT ["python3", "/code/qr_generator.py"]
