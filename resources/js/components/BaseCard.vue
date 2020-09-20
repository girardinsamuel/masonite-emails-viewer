<template>
  <div class="bg-white rounded-md shadow-md">
    <!-- Heading -->
    <div class="px-4 py-2 border-b border-gray-200 rounded-md sm:px-6">
      <div
        class="flex flex-wrap items-center justify-between -mt-2 -ml-4 sm:flex-no-wrap"
      >
        <div class="mt-2 ml-4">
          <h2 class="font-medium leading-4 text-gray-800 text-md">
            {{ title }}
          </h2>
        </div>
        <div class="flex-shrink-0 mt-2 ml-4">
          <slot name="actions">
            <span class="inline-flex rounded-md shadow-sm">
              <button
                type="button"
                class="relative inline-flex items-center px-4 py-2 text-sm font-medium leading-5 text-white bg-indigo-600 border border-transparent rounded-md hover:bg-indigo-500 focus:outline-none focus:shadow-outline-indigo focus:border-indigo-700 active:bg-indigo-700"
              >
                Action 1
              </button>
            </span>
          </slot>
        </div>
      </div>
    </div>
    <!-- Content -->
    <div>
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "BaseCard",
  props: ["title"],
};
</script>
