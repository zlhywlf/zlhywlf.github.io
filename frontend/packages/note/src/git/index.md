# git

## 版本管理

- 版本号的格式为 Major.Minor.Patch
  - 当 API 的兼容性变化时，Major 需递增
  - 当增加功能时(不影响 API 的兼容性)，Minor 需递增
  - 当做 Bug 修复时(不影响 API 的兼容性)，Patch 需递增
- 初始版本号为：v1.0.0

## 分支管理

![git-model](./imgs/git-flow.png)

- master
  - 生产，保护分支，仅接受组长 push
- develop
  - 开发，保护分支，仅接受组长 push
- feature
  - 新特性
  - 从 develop 创建，开发完成合并回 develop，然后删除

  ```bash
    git switch -c myfeature develop
    git switch develop
    git merge --no-ff myfeature
    git branch -d myfeature
    git push origin develop
  ```

- release

  - 预发布
  - 从 develop 创建，开发完成合并回 develop 与 master，然后删除

  ```bash
  git switch -c release-1.2 develop
  git switch master
  git merge --no-ff release-1.2
  git tag 1.2
  git switch develop
  git merge --no-ff release-1.2
  git branch -d release-1.2
  ```

- hotfix

  - bug 修复
  - 从 master 创建，开发完成合并回 release（不存在则为 develop） 与 master，然后删除

  ```bash
  git switch -c hotfix-1.2.1 master
  git switch master
  git merge --no-ff hotfix-1.2.1
  git tag 1.2.1
  git switch develop
  git merge --no-ff hotfix-1.2.1
  git branch -d hotfix-1.2.1
  ```

## 开发流程

1. 组长在 gitlab 建立仓库
2. 组长在本地以 master 初始化仓库，添加 README.md 以及公共资源后做首次提交，添加初始版本标签
3. 组长在本地从 master 创建 develop 并添加开发配置后推送 master 与 develop 到远程
4. 组长在 gitlab 配置
  1. master 允许 Masters 角色 merge，禁止所有角色 push
  2. develop 允许 Masters 角色 merge 与 push
  3. 创建 v\* 标签保护，允许 Masters 角色创建 v 开头的 tag
5. 组长在 gitlab 创建里程碑与任务，从 develop 创建任务对应 feature
6. 组员拉取最新代码到各自 feature 进行开发
7. 组员完成开发后，在对应任务发起 MR，组长审核后合并 feature 至 release（不存在则为 develop），删除 feature
8. 版本开发完成后 release（不存在则从 develop 创建） 做测试，存在 bug 则从 release（不存在则为 develop） 创建任务与对应
   feature 回到第 6 步
9. release 测试完成，组长发起 MR，合并 release 至 develop
10. 组长发起 MR，合并 release 至 master，添加版本标签，删除 release
11. 若 master 出现 bug，组长发起任务，从 master 创建任务对应 hotfix 进行处理
12. hotfix 完成后在对应任务发起 MR，组长审核后合并 hotfix 至 master 与 release（不存在则为 develop），master 添加版本标签

```bash
git clone git@192.168.1.207:algorithm/utility/rapidjson.git
cd rapidjson
touch README.md
echo "# rapidjson" > README.md
git add .
git commit -m "init(rapidjson): Initial commit"
git tag v1.0.0
git switch -c develop
git push origin --all
git push origin --tags
```

不创建mater方式

```bash
mkdir rapidjson && cd rapidjson
git init -b develop
git remote add origin git@192.168.1.207:algorithm/utility/rapidjson.git
```

## 开发

```bash
# 作为库使用
git clone -b 版本号 --depth=1 仓库地址
# 在指定分支开发
git clone -b 分支 仓库地址
```

基本设置

```json
{
  "C_Cpp.default.includePath": [
    "${default}",
    "${workspaceFolder}/**"
  ],
  "C_Cpp.default.configurationProvider": "${default}",
  "C_Cpp.autoAddFileAssociations": false,
  "editor.formatOnSave": true,
  "files.associations": {
    "*.H": "cpp",
    "*.C": "cpp"
  },
  "cmake.configureArgs": [
    "-DDEVELOP_PSO:BOOL=TRUE"
  ]
}
```

## git command

### git branch

#### 创建分支

```bash
git branch develop
# 从远程分支创建
git pull origin dev:dev
```

#### 切换分支

```bash
git switch develop
```

#### 查看所有分支

```bash
git branch -a
```

#### 创建并切换分支

```bash
# 从当前分支创建
git switch -c develop
# 指定提交创建
git switch -c develop commitID
# 创建孤儿分支
git switch --orphan develop
```

#### 推送分支

```bash
# 指定分支
git push origin develop
# 所有分支
git push origin --all
```

#### 删除分支

```bash
# 删除本地 -D 强制删除
git branch -d develop
# 删除远程
git push origin --delete develop
```

#### 关联远程分支

```bash
git branch --set-upstream-to  origin/dev  dev
```

#### 同步远程分支

```bash
git fetch -p
```

### git merge

#### 合并提交

```bash
git merge --squash feature
```

#### 禁止快进

```bash
git merge --no-ff feature
```

### git log

#### 一行查看

```bash
git log --oneline
```

#### 图形化

```bash
git log --graph
```

### git tag

#### 创建标签

```bash
# 当前提交加标签
git tag v1.0.0
# 指定提交加标签
git tag v1.0.0 commitID
```

#### 推送标签

```bash
# 指定
git push origin v1.0.0
# 所有
git push origin --tags
```

#### 删除标签

```bash
git tag -d v1.0.0
```

#### 查看所有标签

```bash
git tag
```

## 常见问题

### 修改最近一次提交信息

```bash
# 拉取需要修改的分支
git clone -b develop git@192.168.1.207:algorithm/utility/rapidjson.git
# 编辑信息，设置 git 编辑器 git config --global core.editor vim
git commit --amend
# 推送到远程，远程分支必须是非保护分支
git push --force-with-lease

```

### 获取提交信息

```bash
# 获取最新commit的hash短值，
# -n表示获得前几条的数据：-1最新一条
# %h表示截取hash值的前一段，%H则表示整个hash值
git log -1 --format="%h"

# 获取最近的tags名称，如果没有tags会获得最新commit的hash短值，如果代码没有git管理则获得空
git describe --abbrev=6 --always --tags
```
