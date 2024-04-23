import { fileURLToPath, URL } from 'node:url';


import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import { VitePWA } from 'vite-plugin-pwa';


export default defineConfig({
    plugins: [
      vue(),
      VitePWA({
        registerType: 'autoUpdate',
        includeAssets: ['favicon.ico', 'robots.txt', 'apple-touch-icon.png'],
        manifest: {
            "name":"sakai-vue",
            "short_name":"sakai-vue",
            "start_url":"/","display":"standalone",
            "background_color":"#ffffff","lang":"en",
            "scope":"/"

        }
      })
    ],
    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url))
      }
    }
  });


