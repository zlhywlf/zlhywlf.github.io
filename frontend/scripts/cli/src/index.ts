import cac from "cac"
import InvalidCommand from "./InvalidCommand"
import CleanProject from "./CleanProject"
import LintProject from "./LintProject"

export default () => {
  try {
    const cli = cac("jsh")
    CleanProject(cli)
    LintProject(cli)
    InvalidCommand(cli)
    cli.help()
    cli.parse()
  } catch (error) {
    console.error((error as Error).stack)
    process.exit(1)
  }
}
