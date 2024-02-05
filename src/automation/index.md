# automation

## 环境准备

docker-compose.yml

```yaml
version: '3.6'
name: "automation"
services:
  gitlab:
    image: 'gitlab/gitlab-ce:12.10.5-ce.0'
    restart: always
    container_name: 'gitlab'
    environment:
      TZ: Asia/Shanghai
      GITLAB_OMNIBUS_CONFIG: |
        external_url 'http://${IP}'
    ports:
      - '80:80'

  gitlab-runner:
    image: 'gitlab/gitlab-runner:v13.12.0'
    restart: always
    container_name: 'gitlab-runner'
    privileged: true
    volumes:
      - ${CONFIG}/focal-sources.list:/etc/apt/sources.list:Z
      - ${CONFIG}/gitlab-runner-bash_profile:/home/gitlab-runner/.bash_profile:Z
      - ${CONFIG}/sdk:/opt:Z
      - /var/run/docker.sock:/var/run/docker.sock
    environment:
      TZ: Asia/Shanghai
      DEMO: DEMO123

  web:
    image: 'ubuntu:20.04'
    container_name: 'web'
    restart: always
    privileged: true
    user: root
    ports:
      - '50070:8080'
    volumes:
      - ${CONFIG}/focal-sources.list:/etc/apt/sources.list:Z
    environment:
      TZ: Asia/Shanghai
    tty: true

networks:
  default:
```

## tmp

```shell


docker pull gitlab/gitlab-runner:v13.12.0

docker run -d --name gitlab-runner --restart always \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v ${CONFIG}/gitlab-runner/config:/etc/gitlab-runner:Z \
  -v ${CONFIG}/config/focal-sources.list:/etc/apt/sources.list:Z \
  -v ${CONFIG}/config/gitlab-runner-bash_profile:/home/gitlab-runner/.bash_profile:Z \
  -v ${CONFIG}/sdk:/opt:Z \
  gitlab/gitlab-runner:v13.12.0

echo 10.255.88.204  git.zdhrsoft.com >> /etc/hosts
su gitlab-runner
bash /opt/Miniconda3-latest-Linux-x86_64.sh
bash /opt/install-nodejs.sh
nvm install --lts
npm install -g pnpm
pnpm config set registry https://registry.npmmirror.com

docker exec -it gitlab-runner bash

docker stop gitlab-runner && docker rm gitlab-runner

gitlab-runner register \
  --non-interactive \
  --url "http://" \
  --registration-token "zV4kKxjPKBue" \
  --executor "shell" \
  --description "demo-shell" \
  --tag-list "build,deploy" \
  --run-untagged="true" \
  --locked="false" \
  --access-level="not_protected"



gitlab-runner unregister --name demo-shell

# gitlab文档
docker run -d --name gitlab-docs --restart always -p 4000:4000 registry.gitlab.com/gitlab-org/gitlab-docs:12.10

docker exec -it gitlab-runner bash -c 'ldd --version && cat /etc/os-release'



gitlab-runner register \
  --non-interactive \
  --url "http:///" \
  --registration-token "sh9NzRcx7KnHJ" \
  --executor "shell" \
  --description "group-shell" \
  --tag-list "build,deploy"




gitlab-runner register \
  --non-interactive \
  --url "http:///" \
  --registration-token "zV4kxjPKBue" \
  --executor "docker" \
  --docker-image "docker:latest" \
  --description "demo-docker" \
  --tag-list "docker-build,docker-deploy" \
  --run-untagged="true" \
  --locked="false" \
  --access-level="not_protected"




  /etc/gitlab-runner/config.toml

[[runners]]
  clone_url = "http://xxxx.xxxx.xxxx.xxxx:9080/" 
  [runners.docker]
    allowed_pull_policies = ["if-not-present"] 
    pull_policy = ["if-not-present"]  
    volumes = ["/var/run/docker.sock:/var/run/docker.sock","/cache"] 
    shm_size = 0


docker load < hangge_server.tar

remote_server=root@156.155.16.12
dir_path=/usr/local/nginx/download
dir_name=omsSystemfront
cd ${dir_path}
echo ${dir_name}
scp ${dir_name}.zip ${remote_server}:/usr/local/nginx/html
ssh ${remote_server} "cd /usr/local/nginx/html;unzip -o ${dir_name}.zip;"
ssh ${remote_server} "rm -f ${dir_name}.zip"
ssh ${remote_server} "/usr/local/nginx/sbin/nginx -s reload"


if [ $(docker ps -aq --filter name=app:latest )]; then docker rm -f app:latest; fi
job:
  stage: deploy
  tags:
    - docker-build
  script:
    - echo $DEMO
    - docker ps
    - docker images
    - docker build . -t app:latest
    - docker save app:latest > app:latest.tar
    - docker rmi app:latest
    - ls -al
```
