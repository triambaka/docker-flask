FROM python:3

#ADD client.py /client/
WORKDIR /app
RUN pip install requests
COPY . .
CMD ["python","-u","client.py"]

#CMD [ "client/client.py" ]


