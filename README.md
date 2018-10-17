# Flask in docker environment 
This repository contains of simple flask app with some endpoints. As well as a docker image.


## DOCKER

### Resources:
* https://semaphoreci.com/community/tutorials/continuous-deployment-of-a-python-flask-application-with-docker-and-semaphore
* https://medium.com/@mtngt/docker-flask-a-simple-tutorial-bbcb2f4110b5
* https://blog.hasura.io/how-to-write-dockerfiles-for-python-web-apps-6d173842ae1d

#### Issues:
* https://unix.stackexchange.com/questions/252684/why-am-i-getting-cannot-connect-to-the-docker-daemon-when-the-daemon-is-runnin 

* Run docker in debug mode:
stop the current demon and start it in debug mode
sudo service docker stop
dockerd -D # --debug

- Display logs from container

`docker logs -f <ID>`

- Start docker: 

Start flask app docker in detached mode
`docker run -d -p 80:80 docker-flask`

`docker start <ID>` or 

#### Development env, docker-compose allows to reload on source code changes 

- Build docker image:

`docker-compose build`

- Run:

`docker-compose up`

- Remove docker image:

`docker-compose down`
    
#### Build with docker env

- Build image:

`docker build -t docker-flask .` optionally add: `--no-cache`

- Remove docker containers:

`docker container prune`

- Tag(commit) and push repository on docker hub

list images: `docker images`

tag: `docker tag cqiot_web ajarzebak/cqiot_web:flask_init`

push: `docker push ajarzebak/cqiot_web:flask_init`

- Create container from image:

`docker container create ajarzebak/cqiot_web:flask_init `

##### Run bash for docker container:

`docker exec -it <ID> /bin/bash`

```
docker-compose build
docker-compose up -d
docker-compose exec app python manage.py recreate_db
```
