# gitlab

## CI/CD

### 启动 runner

```shell
docker run -d --name gitlab-runner --restart always \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v ~/gitlab-runner/config:/etc/gitlab-runner:Z \
  -v ~/config/focal-sources.list:/etc/apt/sources.list:Z \
  -v ~/config/gitlab-runner-bash_profile:/home/gitlab-runner/.bash_profile:Z \
  -v ~/sdk:/opt:Z \
  gitlab/gitlab-runner:v13.12.0
  
# 删除容器
docker stop gitlab-runner && docker rm gitlab-runner

# 查看版本
docker exec -it gitlab-runner bash -c 'ldd --version && cat /etc/os-release'

# gitlab文档
docker run -d --name gitlab-docs --restart always -p 4000:4000 registry.gitlab.com/gitlab-org/gitlab-docs:12.10
```

### 配置 runner

进入容器 `docker exec -it gitlab-runner bash`

```shell
su gitlab-runner
bash /opt/Miniconda3-latest-Linux-x86_64.sh
bash /opt/install-nodejs.sh
nvm install --lts
npm install -g pnpm
pnpm config set registry https://registry.npmmirror.com

# 注册
gitlab-runner register \
  --non-interactive \
  --url "http://gitlab.host.com/" \
  --registration-token "******token******" \
  --executor "shell" \
  --description "demo-shell" \
  --tag-list "build,deploy" \
  --run-untagged="true" \
  --locked="false" \
  --access-level="not_protected"

gitlab-runner register \
  --non-interactive \
  --url "http://gitlab.host.com/" \
  --registration-token "******token******" \
  --executor "shell" \
  --description "group-shell" \
  --tag-list "group-build,group-deploy"
  
# 取消注册
gitlab-runner unregister --name demo-shell
```

