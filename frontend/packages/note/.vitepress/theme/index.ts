import { Catalog } from "./base"
import { h } from "vue"
import DefaultTheme from "vitepress/theme"
import type { Theme } from "vitepress"

export default {
  extends: DefaultTheme,
  Layout() {
    return h(DefaultTheme.Layout, null, {
      "aside-outline-after": () => h(Catalog)
    })
  }
} satisfies Theme
