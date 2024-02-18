# wsl

## 官方手册

[https://learn.microsoft.com/en-us/windows/wsl/install-manual](https://learn.microsoft.com/en-us/windows/wsl/install-manual)

## 启用 wsl

Windows Subsystem for Linux

```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
# 下载 wsl2 升级 https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi
wsl --set-default-version 2
```

## ubuntu 下载

[https://cloud-images.ubuntu.com/releases/](https://cloud-images.ubuntu.com/releases/)

## 安装

```powershell
wsl --import <Distribution Name> <Installation Folder> <Ubuntu WSL2 Image Tarball path>
```

## 删除

```powershell
wsl --unregister <Distribution Name>
```

## 登录

```powershell
wsl -d <Distribution Name>
# 设置默认登录
wsl --set-default <Distribution Name>
```

## 查看

```powershell
wsl -l -v
```

## 终止

```powershell
wsl -t <Distribution Name>
# 所有
wsl --shutdown
```

## 各类配置

### 换源

/etc/apt/sources.list

- ubuntu:18.04

```plain
deb http://mirrors.huaweicloud.com/repository/ubuntu/ bionic main restricted
deb http://mirrors.huaweicloud.com/repository/ubuntu/ bionic-updates main restricted
deb http://mirrors.huaweicloud.com/repository/ubuntu/ bionic universe
deb http://mirrors.huaweicloud.com/repository/ubuntu/ bionic-updates universe
deb http://mirrors.huaweicloud.com/repository/ubuntu/ bionic multiverse
deb http://mirrors.huaweicloud.com/repository/ubuntu/ bionic-updates multiverse
deb http://mirrors.huaweicloud.com/repository/ubuntu/ bionic-backports main restricted universe multiverse
```

- ubuntu:22.04

```plain
deb http://mirrors.huaweicloud.com/repository/ubuntu/ jammy main restricted
deb http://mirrors.huaweicloud.com/repository/ubuntu/ jammy-updates main restricted
deb http://mirrors.huaweicloud.com/repository/ubuntu/ jammy universe
deb http://mirrors.huaweicloud.com/repository/ubuntu/ jammy-updates universe
deb http://mirrors.huaweicloud.com/repository/ubuntu/ jammy multiverse
deb http://mirrors.huaweicloud.com/repository/ubuntu/ jammy-updates multiverse
deb http://mirrors.huaweicloud.com/repository/ubuntu/ jammy-backports main restricted universe multiverse
```

```plain
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-security main restricted universe multiverse
```

```bash
# 更新
apt update
```

### 环境变量

/etc/profile

```plain
# 可执行应用
export JAVA_HOME=/opt/jdk-11.0.15.1
export MAVEN_HOME=/opt/apache-maven-3.8.6
export PATH=$MAVEN_HOME/bin:$JAVA_HOME/bin:$PATH

# 图形应用可视化
# 如果可视化无反应：防火墙 启用 所有 VcXsrv windows xserver 规则
export DISPLAY=$(awk '/nameserver / {print $2; exit}' /etc/resolv.conf 2>/dev/null):0

# 动态库加载路径
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/java/packages/lib
```

### openfoam

```bash
dpkg -i paraviewopenfoam56_0-20190221_amd64.deb
# 安装缺少的依赖
apt-get -f install
```

### C

```bash
apt-get install -y build-essential gdb cmake
```

### java

```bash
tar -zxvf /tmp/jdk-11.0.15.1_linux-x64_bin.tar.gz -C /opt
tar -zxvf /tmp/apache-maven-3.8.6-bin.tar.gz -C /opt
mkdir /root/.m2
# maven 配置
cp /opt/apache-maven-3.8.6/conf/settings.xml /root/.m2
```

/root/.m2/settings.xml

```xml
    <mirror>
        <id>aliyunmaven</id>
        <mirrorOf>central</mirrorOf>
        <name>aliyun</name>
        <url>https://maven.aliyun.com/repository/public</url>
    </mirror>
```

### nodejs

[https://learn.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-wsl](https://learn.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-wsl)

```shell
# 拉取失败可直接复制 install.sh
git clone https://github.com/nvm-sh/nvm.git
cd nvm/
bash install.sh
# 如果没输出 nvm 重启终端
command -v nvm
nvm ls
nvm install --lts
node -v
npm -v
npm install -g pnpm
pnpm config set registry https://registry.npm.taobao.org
```

### mysql

```shell
apt install mysql-server -y
# 首次登陆无密码
mysql -uroot -p
service mysql restart
service mysql start
service mysql status
# 修改root密码
use mysql;
alter user 'root'@'localhost' identified with mysql_native_password by 'root';
flush privileges;
exit;
```

### git

```bash
ssh-keygen -t rsa -C 'tommietanghao@zlhywlf.onmicrosoft.com' -f ~/.ssh/github_id_rsa

# 全局配置用户与邮箱
git config --global user.email tommietanghao@zlhywlf.onmicrosoft.com && \
git config --global user.name zlhywlf

# 默认编辑器
git config --global core.editor vim

# http 方式储存账号密码
git config --global credential.helper store

# 连接测试
ssh -T git@github.com

# 如果报错 Bad owner or permissions on /root/.ssh/config
chmod 600 ~/.ssh/*
```

~/.ssh/config

```plain
Host github.com
HostName github.com
User zlhywlf
PreferredAuthentications publickey
IdentityFile ~/.ssh/github_id_rsa
```

.gitconfig

```plain
[core]
 editor = vim
 autocrlf = true
[credential]
 helper = store
[includeIf "gitdir:~/project/self/"]
 path = ~/.gitconfig_self
[includeIf "gitdir:~/project/work/"]
 path = ~/.gitconfig_work

[user]
 name = zlhywlf
 email = tommietanghao@zlhywlf.onmicrosoft.com
```

### python

```bash
apt install python3-pip python3-tk -y
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
python3 -m venv .venv
pip freeze > requirements.txt
pip install -r requirements.txt
conda list -e > requirements.txt
conda install --yes --file requirements.txt
# 中文字体
# /usr/share/fonts/truetype/noto/SimHei.ttf
```

### vscode

```json
{
    "C_Cpp.default.defines": [
        "NoRepository",
        "linux64",
        "WM_ARCH_OPTION=64",
        "WM_DP",
        "WM_LABEL_SIZE=32"
    ],
    "C_Cpp.default.includePath": [
        "${env:JAVA_HOME}/include/**",
        "${workspaceFolder}/**",
        "/usr/java/packages/include/**"
    ]
}
```

### 字体

```shell
# /usr/share/fonts
mkdir /usr/share/fonts/customFont
cd /usr/share/fonts/customFont
sudo mkfontscale && mkfontdir && fc-cache -fv
```
