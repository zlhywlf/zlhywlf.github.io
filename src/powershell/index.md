# powershell

## 环境变量

### 获取

```powershell
$Env:JAVA_HOME
```

### 当前 process 修改或新增

```powershell
$Env:TMP_VAR = 'TMP'
```

### 持久修改或新增

- Machine
- Process
- User

```powershell
[Environment]::SetEnvironmentVariable('Foo', 'Bar', 'User')
```

### 持久删除

```powershell
[Environment]::SetEnvironmentVariable('Foo', '', 'User')
```
