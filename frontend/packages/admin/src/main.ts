import { createApp } from "vue"
import App from "./App.vue"
import { createVuetify } from "vuetify"

import "vuetify/styles"
import "./core/scss/index.scss"

const app = createApp(App)
app.use(createVuetify({
  theme: {
    defaultTheme: "light"
  }
}))
app.mount("#app")
