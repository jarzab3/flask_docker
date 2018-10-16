FROM python:3.6
MAINTAINER "Adam Jarzebak - ajarzebak@cryptoquantique.com"
ADD . /qt
WORKDIR /qt
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
ENV FLASK_ENV="docker"
ENTRYPOINT [ "python", "app.py" ]
CMD "echo" "Docker run completed!"
