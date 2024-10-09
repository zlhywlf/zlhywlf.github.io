# html(HyperText Markup Language)

## 资源

- [MDN](https://developer.mozilla.org/en-US/)
- [W3C](https://www.w3.org)
- [第一个网站](https://info.cern.ch/hypertext/WWW/TheProject.html)

## 特殊字符

[references](https://developer.mozilla.org/en-US/docs/Glossary/Entity)

## URL 与 URI

- URL: 统一资源定位符 uniform resource locator，俗称网络地址，是 URI 的子集
  - \[协议]://[账户]:[密码]@[地址]:[端口]/[路径]?[查询]#[片段]
- URI: 统一资源标识符 uniform resource identifier，标识逻辑或物理资源

## hello world

- 对文本进行标记，显示形式取决于 css，例如 `h1` 浏览器默认对该标签添加了 css
- 缩进使用 2 个空格

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>html</title>
</head>
<body>
<!-- 注释 -->
<h1>hello world!</h1>
</body>
</html>
```

## vscode 推荐插件

- formulahendry.auto-rename-tag
- formulahendry.auto-close-tag
- ritwickdey.liveserver

## vscode 推荐配置

```json
{
  "editor.tabSize": 2,
  "editor.formatOnSave": true,
  "editor.wordWrap": "on",
  "editor.renderWhitespace": "all"
}
```

## 元素
