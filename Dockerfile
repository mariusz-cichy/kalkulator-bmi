FROM python:alpine3.7
COPY ./static /app/static
COPY ./templates /app/templates
COPY app.py /app
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
