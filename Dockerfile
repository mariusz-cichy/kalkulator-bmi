FROM python:3.8
COPY ./static /app/static
COPY ./templates /app/templates
COPY app.py /app
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 80
CMD python "app.py"
