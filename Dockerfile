FROM python:alpine3.8
WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./1-HelloWorld/epic.py epic.py
ENTRYPOINT [ "python" ]
CMD [ "epic.py" ]