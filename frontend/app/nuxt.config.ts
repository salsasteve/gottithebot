// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
  css: ["vuetify/styles"],
  imports: {
    dirs: ["stores"],
  },
  modules: [
    "@nuxtjs/supabase",
    [
      "@pinia/nuxt",
      {
        autoImports: ["defineStore", "acceptHMRUpdate"],
      },
    ],
  ],
  build: {
    transpile: ["vuetify"],
  },
  runtimeConfig: {
    // Config within public will be also exposed to the client
    public: {
      supabaseUrl: "",
      supabaseKey: "",
    },
  },
});
