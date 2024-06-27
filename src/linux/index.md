# linux

## CentOS7

### 虚拟机网络配置

#### NAT

- edit -> virtual network editor 查看虚拟网络 NAT 的子网 IP: 192.168.184.0
- edit -> virtual network editor 查看虚拟网络 NAT 的子网掩码: 255.255.255.0
- edit -> virtual network editor -> NAT settings 查看网关 IP: 192.168.184.2

```shell
# 查看防火墙状态
systemctl status firewalld
# 关闭防火墙
systemctl stop firewalld
# 禁止开机启动防火墙
systemctl disable firewalld
# 确认网卡配置文件名称: ens33
ip addr
# 修改: BOOTPROTO=none
# 修改: IPV6INIT=no
# 修改: ONBOOT=yes
# 新增: IPADDR=192.168.184.6
# 新增: NETMASK=255.255.255.0
# 新增: GATEWAY=192.168.184.2
# 新增: DNS1=8.8.8.8
vi /etc/sysconfig/network-scripts/ifcfg-ens33
# ssh 登录
ssh root@192.168.184.6
```

### 操作命令

#### 重启

```shell
reboot
```

#### 重启网络

```shell
service network restart
```

#### 修改主机名称

```shell
vi /etc/hostname
```

#### 查看系统用户

```shell
# root:x:0:0:root:/root:/bin/bash
# 用过户名:密码:用户ID:组ID:描述信息:HOME目录:执行终端
getent passwd
```

#### 查看系统组

```shell
# root:x:0:
# 组名称:认证:组ID
getent group
```

### 添加用户

```shell
# 同时新增组 mysql
useradd mysql
```

### 修改文件归属

```shell
# 递归修改
chown -R mysql:mysql directory
```

### 修改用户密码

```shell
passwd mysql
```

### 切换账户

```shell
su - mysql
```

### mysql

[mysql](https://dev.mysql.com/doc/refman/8.4/en/)

#### 下载

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

#### 安装

```shell
useradd mysql
passwd mysql
chown -R mysql:mysql mysql-8.4.0-linux-glibc2.17-x86_64
mv mysql-8.4.0-linux-glibc2.17-x86_64 /home/mysql/mysql-8.4.0
```

#### 配置

```shell
su - mysql
# export PATH=$PATH:/home/mysql/mysql-8.4.0/bin
vi .bash_profile
source .bash_profile
mysql --version
# 获取配置位置: /etc/my.cnf /etc/mysql/my.cnf /usr/local/mysql/etc/my.cnf ~/.my.cnf
mysqld --verbose --help
# 查看启动参数
mysqld --print-defaults
# [mysqld]
# datadir=/home/mysql/data
# socket=/home/mysql/data/mysqld.sock

# [mysqladmin]
# socket=/home/mysql/data/mysqld.sock

# [client]
# socket=/home/mysql/data/mysqld.sock

vi ~/.my.cnf
# 创建数据目录
mkdir ~/data
# 初始化,获取初始密码:  A temporary password is generated for root@localhost: QTAluK9fgz_o
mysqld --initialize
# 启动
nohup mysqld &
# 查看进程
ps -ef | grep mysqld
# 进入 mysql
mysql -uroot -pQTAluK9fgz_o
# 修改默认密码
ALTER USER user() IDENTIFIED BY ''
# 关闭
mysqladmin -uroot -p shutdown
# 创建账户，192.168.184.1 为虚拟机 NAT 所在主机 IP
CREATE USER 'root'@'192.168.184.1' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'192.168.184.1' WITH GRANT OPTION;
```
