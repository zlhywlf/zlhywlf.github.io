import { promises as fs } from "node:fs"
import { join } from "node:path"

export async function deleteFileOrDirectoryRecursively(dir: string, targets: string[]) {
  const items = await fs.readdir(dir)
  for (const item of items) {
    const itemPath = join(dir, item)
    if (targets.includes(item)) {
      await fs.rm(itemPath, { force: true, recursive: true })
      console.log(`Deleted: ${itemPath}`)
      continue
    }
    const stat = await fs.lstat(itemPath)
    if (stat.isDirectory()) {
      await deleteFileOrDirectoryRecursively(itemPath, targets)
    }
  }
}
