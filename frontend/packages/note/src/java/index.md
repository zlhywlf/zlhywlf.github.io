# java

## 环境准备

- [Oracle JDK](https://www.oracle.com/cn/java/technologies/downloads/archive/#JavaSE)
- [Open JDK](https://jdk.java.net/archive/)
- [tutorial](https://docs.oracle.com/javase/tutorial/tutorialLearningPaths.html)

### Windows

1. 下载 `Windows x64 Compressed Archive` 版本
2. 解压到任意目录
3. 添加环境变量 `JAVA_HOME`(see [powershell](../powershell/index#持久修改或新增))
    ```powershell
    [Environment]::SetEnvironmentVariable('JAVA_HOME', '%USERPROFILE%\JDK_DIR', 'User')
    ```
4. 查看 JDK 版本
    ```powershell
    java -version
    ```

## Hello World

<<< @/../../../../backend/java/src/main/java/zlhywlf/jupiter/tutorial/HelloWorld.java
