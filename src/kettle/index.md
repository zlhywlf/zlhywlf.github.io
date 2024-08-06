# pentaho-kettle

- [docs](https://docs.hitachivantara.com/p/pentaho-dia)
- [pentaho-community-edition](https://pentaho.com/pentaho-community-edition)

## 环境准备

```shell
# 1.尽可能为了避免依赖问题,选择 pentaho 官网版本(最新地址见官网)
wget https://privatefilesbucket-community-edition.s3.us-west-2.amazonaws.com/9.2.0.0-290/ce/client-tools/pdi-ce-9.2.0.0-290.zip

# 2.下载源码
# 9.2.0.0-R 即官网版本 9.2.0.0-290
git clone --depth 1 -b 9.2.0.0-R https://github.com/pentaho/pentaho-kettle.git

# 3.按照 pentaho-kettle/README.md 进行构建
# 首先配置好下方 settings.xml (参考 README.md 中提供的 settings.xml)
# 优先使用 aliyun 源,以便提高依赖下载效率
cd pentaho-kettle
mvn clean install -Dmaven.test.skip=true
```

settings.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<settings xmlns="http://maven.apache.org/SETTINGS/1.2.0"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.2.0 https://maven.apache.org/xsd/settings-1.2.0.xsd">
    <mirrors>
        <mirror>
            <id>aliyun</id>
            <name>aliyun public</name>
            <mirrorOf>pentaho-public</mirrorOf>
            <url>https://maven.aliyun.com/repository/public</url>
        </mirror>
        <mirror>
            <id>pentaho</id>
            <mirrorOf>central</mirrorOf>
            <url>https://repo.orl.eng.hitachivantara.com/artifactory/pnt-mvn/</url>
        </mirror>
    </mirrors>

    <profiles>
        <profile>
            <id>pentaho</id>
            <activation>
                <activeByDefault>true</activeByDefault>
            </activation>
            <repositories>
                <repository>
                    <id>pentaho-public</id>
                    <name>Pentaho Public</name>
                    <url>https://repo.orl.eng.hitachivantara.com/artifactory/pnt-mvn/</url>
                    <releases>
                        <enabled>true</enabled>
                        <updatePolicy>always</updatePolicy>
                    </releases>
                    <snapshots>
                        <enabled>true</enabled>
                        <updatePolicy>always</updatePolicy>
                    </snapshots>
                </repository>
            </repositories>
            <pluginRepositories>
                <pluginRepository>
                    <id>pentaho-public</id>
                    <name>Pentaho Public</name>
                    <url>https://repo.orl.eng.hitachivantara.com/artifactory/pnt-mvn/</url>
                    <releases>
                        <enabled>true</enabled>
                        <updatePolicy>always</updatePolicy>
                    </releases>
                    <snapshots>
                        <enabled>true</enabled>
                        <updatePolicy>always</updatePolicy>
                    </snapshots>
                </pluginRepository>
            </pluginRepositories>
        </profile>
    </profiles>

    <pluginGroups>
        <pluginGroup>org.pentaho.maven.plugins</pluginGroup>
        <pluginGroup>com.pentaho.maven.plugins</pluginGroup>
        <pluginGroup>com.github.spotbugs</pluginGroup>
    </pluginGroups>
</settings>
```
