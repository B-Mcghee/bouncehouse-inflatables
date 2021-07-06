<template>
  <div class="bg-black bg-opacity-70 text-white">
    <ul class="grid grid-cols-12">
      <li class="col-span-3 gap-1 border-blue-900 border-2">
        <router-link to="/products">See All</router-link>
      </li>
      <li @click="checkout()" class="col-span-6 gap-1 border-blue-900 border-2">
        Create Reservation
      </li>
      <li class="col-span-3 gap-1 border-blue-900 border-2">
        <router-link to="about">FAQ</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import { checkout } from "../mixins/Mixins";
export default {
  name: "Toolbar",
  mixins: [checkout],
};
</script>

<style>
</style>