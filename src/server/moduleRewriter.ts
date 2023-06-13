import { parse } from '@babel/parser'
import MagicString from 'magic-string'

/**
 *
 * @param source js 代码
 * @param asSFCScript
 * @returns  修改后的 js 代码
 */
export function rewrite(source: string, asSFCScript = false) {
  // 语法解析
  const ast = parse(source, {
    sourceType: 'module',
    plugins: ['bigInt', 'optionalChaining', 'nullishCoalescingOperator']
  }).program.body

  const s = new MagicString(source)

  ast.forEach((node) => {
    // 替换导入语句
    if (node.type === 'ImportDeclaration') {
      if (/^[^\.\/]/.test(node.source.value)) {
        // module import
        // import { foo } from 'vue' --> import { foo } from '/__modules/vue'
        s.overwrite(
          node.source.start!,
          node.source.end!,
          `"/__modules/${node.source.value}"`
        )
      }
    }
    // 替换导出语句
    else if (asSFCScript && node.type === 'ExportDefaultDeclaration') {
      s.overwrite(
        node.start!,
        node.declaration.start!,
        `let __script; export default (__script = `
      )
      s.appendRight(node.end!, `)`)
    }
  })

  return s.toString()
}
