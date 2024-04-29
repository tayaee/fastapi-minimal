FROM python:3.8
COPY requirements.txt /webapp/requirements.txt
COPY main.py /webapp
WORKDIR /webapp
RUN pip install -r requirements.txt
ENTRYPOINT [ "uvicorn" ]
CMD [ "--host": "0.0.0.0", "main:app" ]
