import { defineConfig } from "vite"
import vue from "@vitejs/plugin-vue"
import vuetify, { transformAssetUrls } from "vite-plugin-vuetify"

// https://vite.dev/config/
export default defineConfig({
  base: "./",
  plugins: [
    vue({
      template: { transformAssetUrls }
    }),
    vuetify({
      styles: {
        configFile: "src/core/scss/vuetify.scss"
      }
    })
  ],
  css: {
    preprocessorOptions: {
      sass: {
        api: "modern-compiler"
      }
    }
  }
})
