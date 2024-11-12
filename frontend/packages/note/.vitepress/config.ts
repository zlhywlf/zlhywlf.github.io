import { defineConfigWithTheme } from "vitepress"
import path from "node:path"
import fs from "node:fs"
import { withMermaid } from "vitepress-plugin-mermaid"
import type { DefaultTheme } from "vitepress"

interface Page {
  name: string
  path: string
}

interface CustomThemeConfig extends DefaultTheme.Config {
  pages: Page[]
}

const getPage = (name: string, file: string): Page[] => {
  if (!file.endsWith(".md")) {
    return []
  }
  const fileName = file.replace(".md", "")
  return [{
    name: file.startsWith("index") ? name : `${name}.${fileName}`,
    path: `/${name}/${fileName}.html`
  }]
}

const getRoutes = (name: string, dir = "", isRoot = false): Page[] => {
  const pages: Page[] = []
  dir = isRoot ? path.resolve(name) : dir
  const files = isRoot ? fs.readdirSync(dir).filter(file => file !== "index.md") : fs.readdirSync(dir)
  for (const file of files) {
    const file_dir = path.join(dir, file)
    pages.push(...fs.lstatSync(file_dir).isDirectory() ? getRoutes(file, file_dir) : getPage(name, file))
  }
  return pages
}

export default withMermaid(defineConfigWithTheme<CustomThemeConfig>({
  title: "Note",
  srcDir: "src",
  themeConfig: {
    pages: getRoutes("src", "", true).sort((a, b) => a.name > b.name ? 1 : -1),
    outline: {
      level: [2, 3],
      label: "目录"
    }
  },
  vite: {
    optimizeDeps: {
      include: [
        "mermaid"
      ]
    }
  }
}))
