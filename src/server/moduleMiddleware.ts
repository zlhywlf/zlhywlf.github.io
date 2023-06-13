import path from 'path'
import resolve from 'resolve-cwd'
import { sendJSStream } from './utils'
import { ServerResponse } from 'http'

/**
 * 将依赖库发送到客户端
 *
 * @param id 导入库名称
 * @param res HTTP 响应
 */
export function moduleMiddleware(id: string, res: ServerResponse) {
  let modulePath: string
  try {
    modulePath = resolve(id)
    if (id === 'vue') {
      modulePath = path.join(
        path.dirname(modulePath),
        'dist/vue.runtime.esm-browser.js'
      )
    }
    console.log(modulePath)

    sendJSStream(res, modulePath)
  } catch (e) {
    res.statusCode = 404
    res.end()
  }
}
