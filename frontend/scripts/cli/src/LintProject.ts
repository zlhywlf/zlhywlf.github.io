import type { CAC } from "cac"
import { execa } from "@jupiter/node-util"

export default (cli: CAC) => {
  cli
    .command("lint")
    .usage("检查项目规范")
    .action(async () => {
      await execa({ stdio: "inherit" })`prettier . -w --cache`
    })
}
