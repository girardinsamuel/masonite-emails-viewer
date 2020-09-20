<template>
  <BaseCard title="Parameters">
    <div v-show="mode == 'custom'" class="p-4">
      <div class="flex">
        <textarea
          v-model="jsonstr"
          rows="6"
          class="w-1/2 border border-gray-700 rounded-md"
          ref="jsonText"
          placeholder="Add custom email parameters"
        ></textarea>
        <pre class="w-1/2 p-2 ml-4 bg-gray-400 rounded-md">{{
          prettyCustom
        }}</pre>
      </div>
      <div class="flex justify-end mt-4">
        <button
          @click="updateEmail(jsonstr)"
          class="relative inline-flex items-center px-4 py-2 text-sm font-medium leading-5 transition duration-150 ease-in-out border border-gray-300 rounded-md hover:text-gray-500 focus:z-10 focus:outline-none focus:border-blue-300 focus:shadow-outline-blue active:bg-gray-100 active:text-gray-700"
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
              d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"
            ></path>
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
            ></path>
          </svg>
          Use
        </button>
        <button
          @click="reset"
          class="relative inline-flex items-center px-4 py-2 ml-2 text-sm font-medium leading-5 transition duration-150 ease-in-out border border-gray-300 rounded-md hover:text-gray-500 focus:z-10 focus:outline-none focus:border-blue-300 focus:shadow-outline-blue active:bg-gray-100 active:text-gray-700"
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
              d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"
            ></path>
          </svg>
          Reset
        </button>
      </div>
    </div>
    <div v-show="mode == 'default'" class="p-4">
      <pre class="p-2 bg-gray-400 rounded-md">{{ prettyDefault }}</pre>
    </div>
    <template slot="actions">
      <span class="relative z-0 inline-flex rounded-md shadow-sm">
        <button
          @click="toggleMode('default')"
          type="button"
          class="relative inline-flex items-center px-4 py-2 text-sm font-medium leading-5 transition duration-150 ease-in-out border border-gray-300 rounded-l-md hover:text-gray-500 focus:z-10 focus:outline-none focus:border-blue-300 focus:shadow-outline-blue active:bg-gray-100 active:text-gray-700"
          :class="{
            'text-gray-700 bg-white': mode == 'custom',
            'text-white bg-blue-600': mode == 'default',
          }"
        >
          Default
        </button>
        <button
          @click="toggleMode('custom')"
          type="button"
          class="relative inline-flex items-center px-4 py-2 -ml-px text-sm font-medium leading-5 transition duration-150 ease-in-out border border-gray-300 rounded-r-md hover:text-gray-500 focus:z-10 focus:outline-none focus:border-blue-300 focus:shadow-outline-blue active:bg-gray-100 active:text-gray-700"
          :class="{
            'text-gray-700 bg-white': mode == 'default',
            'text-white bg-blue-600': mode == 'custom',
          }"
        >
          Custom
        </button>
      </span>
    </template>
  </BaseCard>
</template>

<script>
var isObj = function(a) {
  if (!!a && a.constructor === Object) {
    return true;
  }
  return false;
};
var _st = function(z, g) {
  return "" + (g != "" ? "[" : "") + z + (g != "" ? "]" : "");
};
var fromObject = function(params, skipobjects, prefix) {
  if (skipobjects === void 0) {
    skipobjects = false;
  }
  if (prefix === void 0) {
    prefix = "";
  }
  var result = "";
  if (typeof params != "object") {
    return prefix + "=" + encodeURIComponent(params) + "&";
  }
  for (var param in params) {
    var c = "" + prefix + _st(param, prefix);
    if (isObj(params[param]) && !skipobjects) {
      result += fromObject(params[param], false, "" + c);
    } else if (Array.isArray(params[param]) && !skipobjects) {
      params[param].forEach(function(item, ind) {
        result += fromObject(item, false, c + "[" + ind + "]");
      });
    } else {
      result += c + "=" + encodeURIComponent(params[param]) + "&";
    }
  }
  return result;
};

import BaseCard from "./BaseCard.vue";
export default {
  name: "EmailParametersCard",
  components: {
    BaseCard,
  },
  props: {
    defaultParams: {
      type: Object,
      default: () => {},
    },
  },
  data() {
    return {
      mode: "default",
      jsonstr: "",
      jsonerror: "",
      // default
      defaultObject: {},
      prettyDefault: "",
    };
  },
  computed: {
    prettyCustom() {
      // reset error
      this.jsonerror = "";
      let jsonValue = "";
      try {
        // try to parse
        jsonValue = JSON.parse(this.jsonstr);
      } catch (e) {
        this.jsonerror = JSON.stringify(e.message);
        var textarea = this.$refs.jsonText;
        if (this.jsonerror.indexOf("position") > -1) {
          // highlight error position
          var positionStr = this.jsonerror.lastIndexOf("position") + 8;
          var posi = parseInt(
            this.jsonerror.substr(positionStr, this.jsonerror.lastIndexOf('"'))
          );
          if (posi >= 0) {
            textarea.setSelectionRange(posi, posi + 1);
          }
        }
        return "";
      }
      return JSON.stringify(jsonValue, null, 2);
    },
  },
  created() {
    this.defaultObject = JSON.stringify(this.defaultParams);
    this.prettyDefault = this.pretty(this.defaultParams);
    this.loadDefault();
  },
  methods: {
    toggleMode(mode) {
      this.mode = mode;
      if (mode == "default") {
        this.updateEmail(this.defaultObject);
      }
    },
    updateEmail(params) {
      this.$emit("update", fromObject(JSON.parse(params)));
    },
    loadDefault() {
      this.jsonstr = this.defaultObject;
    },
    reset() {
      this.loadDefault();
      this.updateEmail(this.defaultObject);
    },
    pretty(obj) {
      try {
        // try to parse
        return JSON.stringify(obj, null, 2);
      } catch (e) {
        return "";
      }
    },
  },
};
</script>

<style></style>
