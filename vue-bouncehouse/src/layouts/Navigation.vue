<template>
  <header>
    <div>
      <nav class="text-white">
        <div class="bg-black grid grid-cols-12">
          <ul class="grid grid-cols-12 col-span-12 h-12 items-center">
            <li class="col-start-0 col-end-1 text-2xl">
              <router-link to="/">Bounce</router-link>
            </li>
            <li class="col-start-11 col-span-1 text-2xl">&#9776;</li>
          </ul>
        </div>
        <Toolbar />
      </nav>
    </div>
  </header>
</template>

<script>
import Toolbar from "./Toolbar.vue";
export default {
  name: "Navbar",
  components: {
    Toolbar,
  },
};
</script>

<style>
</style>