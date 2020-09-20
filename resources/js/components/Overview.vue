<template>
  <div>
    <p class="mb-6">
      This assistant allows you to preview all <span>Mailable</span> emails you
      created. In addition you will be able to see <strong>HTML</strong> or
      <strong>text</strong> version and <strong>mobile</strong> or
      <strong>desktop</strong> version.
    </p>
    <h2 class="flex items-center mb-2 font-medium text-md">
      <svg
        class="w-6 h-6 mr-2 text-gray-700"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"
        ></path>
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
        ></path>
      </svg>
      Configuration
    </h2>
    <div class="w-1/2 mb-6">
      <div
        v-for="(value, name) in config"
        class="flex items-center justify-between p-2 px-6 mb-2 bg-white rounded-md shadow"
      >
        <span class="font-medium leading-6 text-black">{{ name }}</span>
        <span class="text-gray-700">{{ value }}</span>
      </div>
    </div>

    <h2 class="flex items-center mb-2 font-medium text-md">
      <svg
        class="w-6 h-6 mr-2 text-gray-700"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"
        ></path>
      </svg>
      Statistics
    </h2>
    <div class="inline-block bg-white rounded-lg shadow">
      <div class="inline-block px-4 py-5 sm:p-6">
        <dl>
          <dt class="text-sm font-medium leading-5 text-gray-500 truncate">
            Number of emails
          </dt>
          <dd class="mt-1 text-3xl font-semibold leading-9 text-gray-900">
            {{ number }}
          </dd>
        </dl>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["number", "config"],
};
</script>

<style></style>
