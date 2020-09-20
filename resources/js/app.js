/**
 * First we will load all of this project's JavaScript dependencies which
 * includes Vue and other libraries. It is a great starting point when
 * building robust, powerful web applications using Vue and Masonite.
 */
require("./bootstrap");

window.Vue = require("vue");

// Highlight.js languages (Only required languages)
// import html from "highlight.js/lib/languages/html";
// import json from "highlight.js/lib/languages/json";
import VueHighlightJS from "vue-highlight.js";
/*
 * Import Highlight.js theme
 * Find more: https://highlightjs.org/static/demo/
 */
// Highlight.js languages (All languages)
require("vue-highlight.js/lib/allLanguages");

/*
 * Import Highlight.js theme
 * Find more: https://highlightjs.org/static/demo/
 */
require("highlight.js/styles/default.css");

import { version } from "../../package.json";

Vue.use(VueHighlightJS);

/**
 * The following block of code may be used to automatically register your
 * Vue components. It will recursively scan this directory for the Vue
 * components and automatically register them with their "basename".
 *
 * Eg. ./components/ExampleComponent.vue -> <example-component></example-component>
 */

// const files = require.context("./", true, /\.vue$/i);
// files.keys().map((key) =>
//   Vue.component(
//     key
//       .split("/")
//       .pop()
//       .split(".")[0],
//     files(key).default
//   )
// );

Vue.component("nav-bar", require("./components/Navbar.vue").default);
Vue.component("emails-list", require("./components/EmailsList.vue").default);
Vue.component("container", require("./components/Content.vue").default);

/**
 * Next, we will create a fresh Vue application instance and attach it to
 * the page. Then, you may begin adding components to this application
 * or customize the JavaScript scaffolding to fit your unique needs.
 */
export const eventBus = new Vue();

const app = new Vue({
  el: "#masonite-emails-preview",
  data() {
    return {
      currentEmail: {
        name: null,
        path: null,
      },
      version,
    };
  },
  created() {
    eventBus.$on("select", (email) => {
      this.currentEmail = email;
    });
  },
});

// Vue.config.devtools = true;
