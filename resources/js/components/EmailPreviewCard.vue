<template>
  <div>
    <!-- Header -->
    <BaseCard title="Preview">
      <template slot="actions">
        <span class="relative z-0 inline-flex rounded-md shadow-sm">
          <button
            @click="toggleDisplay('text')"
            type="button"
            class="relative inline-flex items-center px-4 py-2 text-sm font-medium leading-5 transition duration-150 ease-in-out border border-gray-300 rounded-l-md hover:text-gray-500 focus:z-10 focus:outline-none focus:border-blue-300 focus:shadow-outline-blue active:bg-gray-100 active:text-gray-700"
            :class="{
              'text-gray-700 bg-white': mode != 'text',
              'text-white bg-blue-600': mode == 'text',
            }"
          >
            Text
          </button>
          <button
            @click="toggleDisplay('html')"
            type="button"
            class="relative inline-flex items-center px-4 py-2 -ml-px text-sm font-medium leading-5 transition duration-150 ease-in-out border border-gray-300 hover:text-gray-500 focus:z-10 focus:outline-none focus:border-blue-300 focus:shadow-outline-blue active:bg-gray-100 active:text-gray-700"
            :class="{
              'text-gray-700 bg-white': mode != 'html',
              'text-white bg-blue-600': mode == 'html',
            }"
          >
            HTML
          </button>
          <button
            @click="toggleDisplay('code')"
            type="button"
            class="relative inline-flex items-center px-4 py-2 -ml-px text-sm font-medium leading-5 transition duration-150 ease-in-out border border-gray-300 rounded-r-md hover:text-gray-500 focus:z-10 focus:outline-none focus:border-blue-300 focus:shadow-outline-blue active:bg-gray-100 active:text-gray-700"
            :class="{
              'text-gray-700 bg-white': mode != 'code',
              'text-white bg-blue-600': mode == 'code',
            }"
          >
            Code
          </button>
        </span>

        <span class="relative z-0 inline-flex rounded-md shadow-sm">
          <button
            @click="screen = 'desktop'"
            type="button"
            class="relative inline-flex items-center px-4 py-2 text-sm font-medium leading-5 transition duration-150 ease-in-out border border-gray-300 rounded-l-md hover:text-gray-500 focus:z-10 focus:outline-none focus:border-blue-300 focus:shadow-outline-blue active:bg-gray-100 active:text-gray-700"
            :class="{
              'text-gray-700 bg-white': screen != 'desktop',
              'text-white bg-blue-600': screen == 'desktop',
            }"
          >
            Desktop
          </button>
          <button
            @click="screen = 'mobile'"
            type="button"
            class="relative inline-flex items-center px-4 py-2 -ml-px text-sm font-medium leading-5 transition duration-150 ease-in-out border border-gray-300 rounded-r-md hover:text-gray-500 focus:z-10 focus:outline-none focus:border-blue-300 focus:shadow-outline-blue active:bg-gray-100 active:text-gray-700"
            :class="{
              'text-gray-700 bg-white': screen != 'mobile',
              'text-white bg-blue-600': screen == 'mobile',
            }"
          >
            Mobile
          </button>
        </span>

        <span class="inline-flex rounded-md shadow-sm">
          <button
            type="button"
            @click="send"
            class="relative inline-flex items-center px-4 py-2 text-sm font-medium leading-5 text-white transition duration-150 ease-in-out bg-indigo-600 rounded-md focus:z-10 focus:outline-none hover:bg-indigo-700 focus:shadow-outline-blue active:bg-indigo-700 active:text-white"
          >
            <svg
              class="w-4 h-4 mr-2"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"
              ></path>
            </svg>
            {{ sending ? "Sending ..." : "Send" }}
          </button>
        </span>
      </template>
    </BaseCard>
    <!-- Email Preview -->
    <div
      class="mt-4"
      :class="{
        mobile: screen == 'mobile' && mode != 'code',
        desktop: screen == 'desktop' && mode != 'code',
      }"
    >
      <div
        v-show="mode == 'text' && !email.text"
        class="flex items-center p-2 mx-auto text-red-700 bg-red-200 border-red-700 rounded-md"
      >
        <svg
          class="w-6 h-6"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
          ></path>
        </svg>
        <span class="ml-2">No plain text alternative for this email</span>
      </div>
      <p v-show="mode == 'text' && email.text" class="p-4 bg-white rounded-md">
        {{ email.text }}
      </p>
      <div v-show="mode == 'html'" v-html="email.html" class="p-0 bg-white" />
      <!-- <div
        v-show="mode == 'code'"
        class="p-2 bg-gray-400 rounded-md"
        v-html="email.html"
      ></div> -->
      <highlight-code :code="email.html" v-show="mode == 'code'" />
    </div>
  </div>
</template>

<script>
import BaseCard from "./BaseCard.vue";
import { eventBus } from "../app.js";
export default {
  name: "EmailPreviewCard",
  components: {
    BaseCard,
  },
  props: {
    email: {
      type: Object,
      default: () => {},
    },
  },
  data() {
    return {
      mode: "html",
      screen: "desktop",
      sending: false,
    };
  },
  created() {
    eventBus.$on("sent", () => {
      this.sending = false;
    });
  },
  methods: {
    toggleDisplay(mode) {
      this.mode = mode;
    },
    send() {
      this.sending = true;
      this.$emit("send");
    },
  },
};
</script>

<style scoped>
.mobile {
  margin-left: auto;
  margin-right: auto;
  width: 434px;
}
.desktop {
  width: 100%;
}
</style>
