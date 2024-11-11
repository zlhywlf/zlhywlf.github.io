# 表格

## 示例

```css
table {
  border-collapse: collapse;
}

th,
td {
  border: 1px solid #333;
  padding: 0.5rem 1rem;
}

td {
  text-align: center;
}
```

```html

<table>
  <caption>
    title
  </caption>
  <thead>
  <tr>
    <th>id</th>
    <th>name</th>
    <th>age</th>
    <th>memo</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td>1</td>
    <td>foo</td>
    <td>11</td>
    <!-- 跨行合并 -->
    <td rowspan="2">memo</td>
  </tr>
  <tr>
    <td>2</td>
    <td>bar</td>
    <td>16</td>
  </tr>
  </tbody>
  <tfoot>
  <tr>
    <!-- 跨列合并 -->
    <td colspan="4">foot</td>
  </tr>
  </tfoot>
</table>
```

<table>
  <caption>
    title
  </caption>
  <thead>
    <tr>
      <th>id</th>
      <th>name</th>
      <th>age</th>
      <th>memo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>foo</td>
      <td>11</td>
      <td rowspan="2">memo</td>
    </tr>
    <tr>
      <td>2</td>
      <td>bar</td>
      <td>16</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td colspan="4">foot</td>
    </tr>
  </tfoot>
</table>
