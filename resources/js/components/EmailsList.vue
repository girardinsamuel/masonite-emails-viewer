<template>
  <div class="flex flex-col w-64">
    <!-- Sidebar component, swap this element with another sidebar if you like -->
    <div class="flex flex-col flex-1 h-0 border-r border-gray-400">
      <div class="flex flex-col flex-1 pt-5 pb-4 overflow-y-auto">
        <nav class="flex-1 px-2 mt-5 space-y-1">
          <a
            v-for="email in emails"
            :key="email.name"
            @click="select(email)"
            class="flex items-center px-2 py-2 text-sm font-medium leading-5 transition duration-150 ease-in-out rounded-md cursor-pointer group hover:text-gray-900 hover:bg-gray-100 focus:outline-none focus:bg-gray-200"
            :class="{
              'bg-white text-black border-l-2 rounded-l-none border-blue-600':
                current == email.name,
              'text-gray-900 bg-transparent': current !== email.name,
            }"
          >
            {{ email.name }}
          </a>
        </nav>
      </div>
    </div>
  </div>
</template>

<script>
import { eventBus } from "../app.js";
export default {
  name: "EmailsList",
  props: {
    emails: {
      type: Array,
      default: () => [],
    },
  },
  computed: {
    current() {
      return this.$root.$data.currentEmail.name;
    },
  },
  methods: {
    select(email) {
      eventBus.$emit("select", email);
    },
  },
};
</script>

<style></style>
