# html(HyperText Markup Language)

## 资源

- [MDN](https://developer.mozilla.org/en-US/)
- [W3C](https://www.w3.org)
- [第一个网站](https://info.cern.ch/hypertext/WWW/TheProject.html)

## 字符实体

[references](https://developer.mozilla.org/en-US/docs/Glossary/Entity)

## URL 与 URI

- URL: 统一资源定位符 uniform resource locator，俗称网络地址，是 URI 的子集
  - \[协议]://[账户]:[密码]@[地址]:[端口]/[路径]?[查询]#[片段]
- URI: 统一资源标识符 uniform resource identifier，标识逻辑或物理资源

## 搜索引擎优化 SEO search engine optimization

尽可能使用语义化标签

## hello world

- 对文本进行标记，显示形式取决于 css，例如 `h1` 浏览器默认对该标签添加了 css
- 缩进使用 2 个空格

```html
<!DOCTYPE html> <!-- 文档声明，必须在首位 -->

<html lang="en"> <!-- 根元素，简体中文使用 lang="zh-CN" -->

<head> <!-- 页面配置 -->
  <meta charset="UTF-8" /> <!-- 元数据——网页编码 -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0" /> <!-- 元数据——视图宽度与缩放比例 -->
  <title>html</title> <!-- 页面标题 -->
</head>

<body> <!-- 页面具体内容与结构 -->
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

### 标题 `h1` ~ `h6` (headline)

标记文本标题，默认 `h1` 标题最大， `h6` 最小

```html
<h1>title</h1>
<h2>title</h2>
<h3>title</h3>
<h4>title</h4>
<h5>title</h5>
<h6>title</h6>
```

```css
/* 浏览器添加的默认 css */
h1 {
  display: block;
  font-size: 2em;
  margin-block-start: 0.67em;
  margin-block-end: 0.67em;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
  font-weight: bold;
  unicode-bidi: isolate;
}

h6 {
  display: block;
  font-size: 0.67em;
  margin-block-start: 2.33em;
  margin-block-end: 2.33em;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
  font-weight: bold;
  unicode-bidi: isolate;
}
```

### 段落 `p` (paragraph)

标记文本段落

```html
<p>paragraph</p>
```

### 图像 `img` (image)

加载 `src` 指定的图像资源，当不能被加载时，将显示 `alt` 的值

```html
<img src="/path" alt="image">
```

### 链接跳转-锚 `a` (anchor)

跳转至 `href` 指定的位置

```html
<a href="#id">text</a>
```

### 嵌套其他 html 文档 `iframe` (inline framework)

```html

<iframe src="https://example.org" title="iframe Example 1" width="400" height="300"></iframe>
```

### 独占一行 `div` (division)

无语义，需要将内容独占一行使用

```html

<div>division</div>
```

### 标记一行中部分内容 `span` (span)

```html

<div>div<span>is</span>ion</div>
```
