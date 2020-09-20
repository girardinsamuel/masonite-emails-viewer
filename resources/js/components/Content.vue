<template>
  <main class="w-full mx-auto max-w-7xl sm:p-6 lg:p-8">
    <overview
      v-if="current.name === null"
      :number="emails.length"
      :config="config"
    />
    <email-content v-else :email="current" />
  </main>
</template>

<script>
import EmailContent from "./EmailContent.vue";
import Overview from "./Overview.vue";

export default {
  name: "Content",
  components: {
    EmailContent,
    Overview,
  },
  props: {
    emails: {
      type: Array,
      default: () => [],
    },
    config: {
      type: Object,
      default: () => {},
    },
  },
  computed: {
    current() {
      return this.$root.$data.currentEmail;
    },
  },
};
</script>

<style></style>
