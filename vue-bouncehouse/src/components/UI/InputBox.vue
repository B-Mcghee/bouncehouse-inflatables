<template>
  <input
    :type="mode"
    class="
      border-2 border-gray-200
      focus:ring-2 focus:ring-gray-600
      focus:outline-none
      w-72
      rounded-lg
    "
  />
</template>

<script>
export default {
  name: "Input",
  props: {
    mode: {
      default: "text",
    },
  },
};
</script>

<style>
</style>