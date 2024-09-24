import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

const isProd = process.env.NODE_ENV === 'production'

// https://vitejs.dev/config/
export default defineConfig({ 
  base: process.env.BASE_URL ?? '/dev/',
  server: {
    hmr: !isProd,
    host: true,
    port: parseInt(process.env.PORT ?? "3000"),
    watch: isProd ? null : undefined, // Null disables the file watcher, undefined uses default
    proxy: {
      '/dev/api': {
        target: 'http://localhost:5000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/dev\/api/, '')
      }
    }
  },
  plugins: [
    vue(),
    vueDevTools(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
