import type { CAC } from "cac"
import { deleteFileOrDirectoryRecursively } from "@jupiter/node-util"

export default (cli: CAC) => {
  cli
    .command("clean")
    .usage("清理项目目录")
    .option("--del-lock", "删除 pnpm-lock.yaml", { default: false })
    .action(async ({ delLock = false }) => {
      const targets = ["node_modules", "dist", "cache", ...(delLock ? ["pnpm-lock.yaml"] : [])]
      const rootDir = process.cwd()
      console.log(`Starting cleanup of targets: ${targets.join(", ")} from ${rootDir}`)
      await deleteFileOrDirectoryRecursively(rootDir, targets)
    })
}
