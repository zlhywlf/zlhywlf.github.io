import type { CAC } from "cac"

export default (cli: CAC) => {
  cli.on("command:*", () => {
    console.error("Invalid command: %s", cli.args.join(" "))
    process.exit(1)
  })
}
