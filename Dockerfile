FROM python:3.8
COPY requirements.txt /handleFilesApplication/requirements.txt
WORKDIR /handleFilesApplication
RUN pip install -r requirements.txt
COPY . /handleFilesApplication
VOLUME /tmp
ENTRYPOINT ["python"]
CMD ["main.py"]