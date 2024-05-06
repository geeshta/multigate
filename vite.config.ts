import vue from "@vitejs/plugin-vue";

import { defineConfig } from "vite";

import vuetify from "vite-plugin-vuetify";

import path from "path";

const ROOT = path.join(__dirname, "frontend");

// https://vitejs.dev/config/
export default defineConfig({
  root: ROOT,
  plugins: [vue(), vuetify()],
  envDir: path.resolve(__dirname),
  server: {
    port: 5300,
    strictPort: true,
    cors: true
  },
  build: {
    emptyOutDir: true,
    target: "es2022",
    assetsDir: "static"
  }
});
