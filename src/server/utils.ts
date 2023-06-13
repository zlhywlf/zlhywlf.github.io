import fs from 'fs'
import { ServerResponse } from 'http'

export function send(
  res: ServerResponse,
  source: string | Buffer,
  mime: string
) {
  res.setHeader('Content-Type', mime)
  res.end(source)
}

export function sendJS(res: ServerResponse, source: string | Buffer) {
  send(res, source, 'application/javascript')
}

export function sendJSStream(res: ServerResponse, filename: string) {
  res.setHeader('Content-Type', 'application/javascript')
  const stream = fs
    .createReadStream(filename)
    // 发生错误时触发
    .on('error', (err) => {
      res.end(err)
    })

  // 打开文件时触发
  stream.on('open', () => {
    // 以流的方式进行响应
    stream.pipe(res)
  })
}
