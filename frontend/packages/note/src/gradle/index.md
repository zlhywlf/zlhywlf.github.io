# 环境准备

## 参考资料

[gradle官网](https://gradle.org/)

[配置阿里源](https://developer.aliyun.com/mvn/guide)

## 配置环境变量

### Windows

- 添加：GRADLE_HOME = %USERPROFILE%\SDK\gradle-8.5
- 修改：PATH += %GRADLE_HOME%\bin

## 查看版本

```shell
gradle -v
```

## 仓库源配置

- windows：%USERPROFILE%\\.gradle\\init.gradle
- linux：~/.gradle/init.gradle

```groovy
// org.gradle.api.invocation.Gradle
allprojects {
    repositories {
        maven {
            name 'aliyun'
            url 'https://maven.aliyun.com/repository/public/'
        }
        mavenLocal()
        mavenCentral()
    }
}
```

## 创建项目

### Windows

```shell
mkdir demo;`
cd demo;`
New-Item settings.gradle;`
gradle wrapper --gradle-distribution-url https://mirrors.cloud.tencent.com/gradle/gradle-8.5-bin.zip
```

## 常见命令

- `gradle classes`：编译源码（build/classes 与 build/resources）
- `gradle clean`：清理构建文件（build）
- `gradle test`：执行测试，并生成测试报告（build/reports）
- `gradle build`：打包（build/libs）
- `gradle build -x test`：打包时跳过测试
- `gradle properties`：查看全局属性

## 项目配置

### settings.gradle

org.gradle.api.initialization.Settings

### build.gradle

org.gradle.api.Project