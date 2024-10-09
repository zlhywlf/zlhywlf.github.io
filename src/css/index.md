# css(Cascading Style Sheet)

## 资源

- [MDN](https://developer.mozilla.org/en-US/)
- [W3C](https://www.w3.org)
- [Emmet](https://docs.emmet.io/cheat-sheet/)
- [caniuse](https://caniuse.com)

## 定义位置

- 内联样式 inline style sheet：定义在元素 `style` 属性中
- 内部样式 internal style sheet：定义在文档 `style` 元素中
  ```html
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <style>
        body {transition: opacity ease-in 0.2s; }
      </style>
    </head>
  </html>
  ```
- 外部样式 external style sheet：定义在外部文件，由 `link` 元素引入
  ```html
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <link rel="stylesheet" href="/index.600a2369.css">
    </head>
  </html>
  ```

# 文本

- 行高：两行文字基线(baseline)之间的距离
- 字体大小：所占空间在顶线与底线之间
- 单位
  - em: 相对于当前或父元素的字体大小
  - rem: 相对于根元素的字体大小

## 定位元素

- 通用
  ```css
  /* 选中所有元素，多个 */
  * {
  }
  ```
- 元素
  ```css
  /* 选中所有 p 元素，零个或多个 */
  p {
  }
  ```
- id
  ```css
  /* 选中 id 为 bar 的元素，零个或一个 */
  #foo {
  }
  ```
- 类
  ```css
  /* 选中类存在 bar 的元素，零个或多个 */
  .bar {
  }
  ```
- 属性
  ```css
  /* 选中存在属性 title 的元素，零个或多个 */
  [title] {
  }
  /* 选中存在属性 title 且值为 foo 的元素，零个或多个 */
  [title=foo] {
  }
  /* 选中存在属性 title 且值包含 foo 的元素，零个或多个 */
  [title*=foo] {
  }
  /* 选中存在属性 title 且值以 foo 开头的元素，零个或多个 */
  [title^=foo] {
  }
  /* 选中存在属性 title 且值以 foo 结尾的元素，零个或多个 */
  [title$=foo] {
  }
  /* 选中存在属性 title 且值为 foo 或者以 foo 开头且紧跟连接符 - 的元素，零个或多个 */
  [title|=foo] {
  }
  /* 选中存在属性 title 且值包含 foo 的元素，如果有其他值必须以空格和 foo 分割，零个或多个 */
  [title~=foo] {
  }
  ```
- 组合
  ```css
  /* 后代，存在类 bar 的元素内部所有 p 元素 */
  .bar p{
  }
  /* 直接后代，存在类 bar 的元素内部第一层所有 p 元素 */
  .bar > p{
  }
  /* 兄弟，存在类 bar 的元素同级所有 p 元素 */
  .bar ~ p{
  }
  /* 相邻兄弟，存在类 bar 的元素同级第一个 p 元素 */
  .bar + p{
  }
  /* 交集，存在类 bar 的 p 元素 */
  p.bar{
  }
  /* 并集，存在类 bar 的元素或 p 元素 */
  p , .bar{
  }
  ```
- 伪类 Pseudo-classes
  ```css
  /* 鼠标处于 div 元素上时 */
  div:hover {
  }
  ```
- 伪元素 Pseudo-elements
  ```css
  /* 首行 */
  ::first-line {
  }
  ```

## 选择器权重

- !important: 10000
- 内联样式: 1000
- id选择器: 100
- 类选择器、属性选择器、伪类: 10
- 元素选择器、伪元素: 1
- 通用选择器: 0
