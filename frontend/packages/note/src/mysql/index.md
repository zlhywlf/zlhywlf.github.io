# mysql

[mysql](https://dev.mysql.com/doc/refman/8.4/en/)

## 下载

[downloads](https://dev.mysql.com/downloads/)

```shell
# 查看 GLIBC 版本: ldd (GNU libc) 2.17
# 下载: mysql-8.4.0-linux-glibc2.17-x86_64.tar.xz
ldd --version
yum install -y wget
wget https://cdn.mysql.com//Downloads/MySQL-8.4/mysql-8.4.0-linux-glibc2.17-x86_64.tar.xz
# 解压缩
xz -d mysql-8.4.0-linux-glibc2.17-x86_64.tar.xz
tar xf mysql-8.4.0-linux-glibc2.17-x86_64.tar
```

## 安装

### linux

```shell
useradd mysql
chown -R mysql:mysql mysql-8.4.0-linux-glibc2.17-x86_64
mv mysql-8.4.0-linux-glibc2.17-x86_64 /home/mysql/mysql-8.4.0
```

### docker

```shell
docker run --name=mysql8.4 --restart on-failure -d container-registry.oracle.com/mysql/community-server:8.4
# 获取初始密码
docker logs mysql8.4 2>&1 | grep GENERATED
docker exec -it mysql8.4 mysql -uroot -p
```

## 配置

```shell
su - mysql
sed -i '/export PATH/c export PATH=$PATH:/home/mysql/mysql-8.4.0/bin' ~/.bash_profile
source .bash_profile
mysql --version
# 获取配置位置
mysqld --verbose --help | grep my.cnf
# 查看启动参数
mysqld --print-defaults
# 创建数据目录
mkdir ~/data
# 配置
echo -e "\
[mysqld]\n\
datadir=/home/mysql/data\n\
socket=/home/mysql/data/mysqld.sock\n\
\n\
[mysqladmin]\n\
socket=/home/mysql/data/mysqld.sock\n\
\n\
[client]\n\
socket=/home/mysql/data/mysqld.sock\n\
" > ~/.my.cnf
# 初始化,获取初始密码:  A temporary password is generated for root@localhost: VYQdkraQa1*#
mysqld --initialize
# 启动
nohup mysqld &
# 查看进程
ps -ef | grep mysqld
# 进入 mysql
mysql -uroot -pVYQdkraQa1*#
# 修改默认密码
ALTER USER user() IDENTIFIED BY '';
# 创建远程root账户
CREATE USER 'root'@'192.168.184.1' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'192.168.184.1' WITH GRANT OPTION;
# 关闭
mysqladmin -uroot -p shutdown
```
