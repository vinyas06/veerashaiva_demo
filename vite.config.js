import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { resolve } from 'node:path'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    rollupOptions: {
      input: {
        main: resolve(import.meta.dirname, 'index.html'),
        blinker: resolve(import.meta.dirname, 'blinker/index.html'),
        niranthara: resolve(import.meta.dirname, 'niranthara/index.html'),
        veerashaivaExpressLogistics: resolve(import.meta.dirname, 'veerashaiva-express-logistics/index.html'),
        veerashaivaInfotechTechnology: resolve(import.meta.dirname, 'veerashaiva-infotech-technology/index.html'),
        coastalKing: resolve(import.meta.dirname, 'coastal-king/index.html'),
      },
    },
  },
})
