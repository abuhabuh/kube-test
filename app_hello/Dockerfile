FROM ubuntu-python

COPY requirements.txt /app/requirements.txt
COPY src/app.py /app/app.py

RUN pip install -r /app/requirements.txt

EXPOSE 12046

ENTRYPOINT python /app/app.py
