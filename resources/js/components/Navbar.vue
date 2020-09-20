<template>
  <nav class="border-b border-gray-400">
    <div class="px-4 mx-auto max-w-7xl sm:px-6 lg:px-8">
      <div class="flex justify-between h-16">
        <div class="flex">
          <div class="flex items-center flex-shrink-0">
            <img
              class="block w-auto h-8"
              src="https://gblobscdn.gitbook.com/spaces%2F-L9uc-9XAlqhXkBwrLMA%2Favatar.png?alt=media"
              alt="Workflow logo"
            />
            <a href="/emails">
              <h1 class="ml-6 font-medium text-md">
                Masonite Emails Debugger
              </h1>
            </a>
            <span class="px-1 ml-4 text-xs text-gray-600 bg-gray-400 rounded-sm"
              >v{{ version }}</span
            >
          </div>
        </div>
        <div class="flex items-center ml-6">
          <span class="inline-flex ml-3 rounded-md shadow-sm">
            <button
              type="button"
              class="relative inline-flex items-center px-4 py-2 text-sm font-medium leading-5 text-blue-400 border border-blue-600 rounded-md hover:text-gray-500 focus:outline-none focus:shadow-outline-blue active:bg-gray-50 active:text-gray-800"
            >
              <svg
                class="w-4 h-4"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"
                ></path>
              </svg>
            </button>
          </span>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Navbar",
  methods: {
    refresh() {
      document.location.reload(true);
    },
  },
  computed: {
    version() {
      return this.$root.$data.version;
    },
  },
};
</script>

<style></style>
