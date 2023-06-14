const fss = require('fs')
const fs = require('fs').promises
const path = require('path')
const execa = require('execa')
const puppeteer = require('puppeteer')

const timeout = (n) => new Promise((r) => setTimeout(r, n))

const fixtureDir = path.join(__dirname, 'fixtures')
const tempDir = path.join(__dirname, 'temp')
let server
let browser

jest.setTimeout(10000)

beforeAll(async () => {
  if (fss.existsSync(tempDir)) {
    await fs.rm(tempDir, { recursive: true })
  }
  await fs.mkdir(tempDir)
  for (const file of await fs.readdir(fixtureDir)) {
    await fs.copyFile(
      path.join(__dirname, 'fixtures', file),
      path.join(tempDir, file)
    )
  }
})

afterAll(async () => {
  await fs.rm(tempDir, { recursive: true })
  if (browser) {
    await browser.close()
  }
  if (server) {
    server.kill('SIGTERM', {
      forceKillAfterTimeout: 2000
    })
  }
})

test('test', async () => {
  server = execa('node', [path.resolve(__dirname, '../bin/vite.js')], {
    cwd: tempDir
  })

  await new Promise((resolve) => {
    server.stdout.on('data', (data) => {
      if (data.toString().match('Running')) {
        resolve()
      }
    })
  })

  browser = await puppeteer.launch(
    process.platform === 'linux'
      ? {
          headless: 'new',
          args: ['--no-sandbox', '--disable-setuid-sandbox']
        }
      : {}
  )
  const page = await browser.newPage()
  await page.goto('http://localhost:3000')
  const button = await page.$('button')
  expect(await button.evaluate((b) => b.textContent)).toBe('0')
  const child = await page.$('.child')
  expect(await child.evaluate((e) => e.textContent)).toBe('This is child')
  await button.click()
  expect(await button.evaluate((b) => b.textContent)).toBe('1')
  const compPath = path.join(tempDir, 'Comp.vue')
  const content = await fs.readFile(compPath, 'utf-8')
  await fs.writeFile(
    compPath,
    content.replace('{{ count }}', 'count is {{ count }}')
  )
  await timeout(200)
  const text = await button.evaluate((b) => b.textContent)
  expect(text).toBe('count is 1')
})
