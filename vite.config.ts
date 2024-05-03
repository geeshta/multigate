import vue from "@vitejs/plugin-vue";

import { defineConfig } from "vite";

import vuetify from "vite-plugin-vuetify";

import litestar from "litestar-vite-plugin";

import path from "path";

const ROOT = path.join(__dirname, "frontend");
const BE_ROOT = path.join(ROOT, "server", "src", "multigate");

const litestarPlugin = litestar({
  input: [path.join(ROOT, "src", "main.ts")],
  resourceDirectory: path.join(__dirname, "src"),
  hotFile: path.join(ROOT, "public", "hot")
});

// https://vitejs.dev/config/
export default defineConfig({
  root: ROOT,
  base: "/static/",
  plugins: [vue(), vuetify(), litestarPlugin],
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
