# Dockerfile - this is a comment. Delete me if you want.
FROM python:3.6

WORKDIR /app

RUN pip install Flask
COPY . .
EXPOSE 5000
CMD ["python","-u","server.py"]

#ENTRYPOINT ["python"]
#CMD ["server/server.py"]

