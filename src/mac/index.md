## brew
https://gitee.com/cunkai/HomebrewCN

brew install --cask docker visual-studio-code

## 资源
镜像加速器：https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors

ubuntu 源：https://developer.aliyun.com/mirror/ubuntu

ubuntu 包：http://security.ubuntu.com/ubuntu/pool/main/

dpkg -i /softwares/ca-certificates_20230311ubuntu0.22.04.1_all.deb

## ubuntu
docker run --privileged -itd -v ~/Docker/sources.list.22.04:/etc/apt/sources.list:ro -v ~/.ssh:/root/.ssh:ro -v /usr/share/zoneinfo/Asia/Chongqing:/etc/localtime:ro -v ~/Docker/softwares:/softwares --name=cpython ubuntu:22.04

docker run --privileged -itd -v ~/.ssh:/root/.ssh:ro -v /usr/share/zoneinfo/Asia/Chongqing:/etc/localtime:ro --name=cpython ubuntu:22.04

## nodejs
docker run --privileged -itd -p 5173:5173 -v ~/.ssh:/root/.ssh:ro -v /usr/share/zoneinfo/Asia/Chongqing:/etc/localtime:ro --name=node2011 node:20.11.1

npm install -g pnpm && pnpm config set registry https://registry.npmmirror.com

## python
docker run --privileged -itd -p 5174:5000 -v ~/.ssh:/root/.ssh:ro -v /usr/share/zoneinfo/Asia/Chongqing:/etc/localtime:ro --name=python312 python:3.12
