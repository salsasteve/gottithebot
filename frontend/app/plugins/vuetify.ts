import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import { aliases, fa } from "vuetify/iconsets/fa";
import { mdi } from "vuetify/iconsets/mdi";

export default defineNuxtPlugin((nuxt) => {
  const vuetify = createVuetify({
    icons: {
      defaultSet: "fa",
      aliases,
      sets: {
        fa,
        mdi,
      },
    },
    ssr: true,
    components,
    directives,
  });
  nuxt.vueApp.use(vuetify);
});
