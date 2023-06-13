import { promises as fs } from 'fs'
import path from 'path'
import http, { Server } from 'http'
import serve from 'serve-handler'
import url from 'url'
import WebSocket from 'ws'
import { sendJS } from './utils'
import { moduleMiddleware } from './moduleMiddleware'
import { rewrite } from './moduleRewriter'
import { vueMiddleware } from './vueMiddleware'
import { createFileWatcher } from './hmrWatcher'

export interface ServerConfig {
  port?: number
  cwd?: string
}

export async function createServer({
  port = 3000
}: ServerConfig = {}): Promise<Server> {
  // WebSocket 客户端代码 Buffer
  const hmrClientCode = await fs.readFile(
    path.resolve(__dirname, '../client/client.js')
  )

  /**
   * **********************************************
   * http
   * **********************************************
   */

  // 创建 http.Server 实例，并添加 requestListener
  // https://nodejs.org/api/http.html
  const server = http.createServer(async (req, res) => {
    // 获取请求资源路径
    // ! 非空断言
    // const pathname = new URL(req.url!, `http://${req.headers.host!}`).pathname
    const pathname = url.parse(req.url!, true).pathname!
    if (pathname === '/__hmrClient') {
      // 处理 WebSocket 客户端
      return sendJS(res, hmrClientCode)
    } else if (pathname.startsWith('/__modules/')) {
      // 处理依赖
      return moduleMiddleware(pathname.replace('/__modules/', ''), res)
    } else if (pathname.endsWith('.vue')) {
      // 处理 vue 类型文件
      return vueMiddleware(req, res)
    } else if (pathname.endsWith('.js')) {
      const filename = path.join(process.cwd(), pathname.slice(1))
      try {
        const content = await fs.readFile(filename, 'utf-8')
        // 重写导入导出
        return sendJS(res, rewrite(content))
      } catch (e) {
        if (e.code === 'ENOENT') {
          serve(req, res)
        } else {
          console.error(e)
        }
      }
    }

    serve(req, res, {
      rewrites: [{ source: '**', destination: '/index.html' }]
    })
  })

  /**
   * **********************************************
   * WebSocket
   * **********************************************
   */

  // 开启 WebSocket 服务
  const wss = new WebSocket.Server({ server })

  const sockets = new Set<WebSocket>()
  wss.on('connection', (socket) => {
    sockets.add(socket)
    socket.send(JSON.stringify({ type: 'connected' }))
    socket.on('close', () => {
      sockets.delete(socket)
    })
  })

  wss.on('error', (e: Error & { code: string }) => {
    if (e.code !== 'EADDRINUSE') {
      console.error(e)
    }
  })

  wss.on('close', () => {
    console.log('close')
  })

  /**
   * **********************************************
   * fileWatcher
   * **********************************************
   */
  createFileWatcher((payload) =>
    sockets.forEach((s) => s.send(JSON.stringify(payload)))
  )

  return new Promise((resolve, reject) => {
    server.on('error', (e: Error & { code: string }) => {
      if (e.code === 'EADDRINUSE') {
        console.log(`port ${port} is in use, trying another one...`)
        setTimeout(() => {
          server.close()
          server.listen(++port)
        }, 100)
      } else {
        console.error(e)
        reject(e)
      }
    })

    server
      .on('listening', () => {
        console.log(`Running at http://localhost:${port}`)
        resolve(server)
      })
      // 设置端口
      .listen(port)
  })
}
