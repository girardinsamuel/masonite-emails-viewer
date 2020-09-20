<template>
  <div v-if="loading">
    <p class="text-lg text-center">Loading ...</p>
  </div>
  <div v-else class="pb-10">
    <h2 class="mb-2 text-lg font-medium leading-6 text-black">
      {{ email.name }}
    </h2>
    <p class="mb-4 text-gray-700">{{ email.path }}</p>
    <EmailPreviewCard
      class="mb-10"
      :email="emailPreview"
      @send="sendTestEmail"
    />
    <EmailParametersCard
      @update="updateEmailPreview"
      :default-params="emailPreview.defaultParams"
    />
  </div>
</template>

<script>
import EmailPreviewCard from "./EmailPreviewCard.vue";
import EmailParametersCard from "./EmailParametersCard.vue";
import { eventBus } from "../app.js";

export default {
  name: "EmailContent",
  components: {
    EmailPreviewCard,
    EmailParametersCard,
  },
  props: {
    email: {
      type: Object,
      default: () => {},
    },
  },
  data() {
    return {
      emailPreview: {
        text: "",
        html: "",
        defaultParams: {},
      },
      loading: true,
    };
  },
  methods: {
    updateEmailPreview(parameters) {
      console.log(parameters);
      this.getEmailPreview(this.email.name, parameters);
    },
    getEmailPreview(emailName, params = null) {
      window.axios
        .get(`/emails/${emailName}/${params ? "?" + params : ""}`)
        .then((emailResponse) => {
          this.emailPreview.html = emailResponse.data.html;
          this.emailPreview.text = emailResponse.data.text;
          this.emailPreview.defaultParams = emailResponse.data.default_params;
          this.loading = false;
        })
        .catch(() => {
          debugger;
          this.loading = false;
        });
    },
    sendTestEmail() {
      window.axios.post(`/emails/${this.email.name}/send`).then(() => {
        eventBus.$emit("sent");
      });
    },
  },
  created() {
    this.getEmailPreview(this.email.name);
  },
};
</script>

<style></style>
