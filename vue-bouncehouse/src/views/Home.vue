<template>
  <main class="container mx-auto">
    <div class="my-8">
      <h1 class="text-4xl">Bounce With Us Inflatables</h1>
    </div>
    <figure></figure>
    <img
      class="w-full"
      :src="require(`@/assets/images/tropical_slide/${image}`)"
      alt=""
    />
    <section
      class="bg-black h-auto overflow-x-scroll items-center align-middle"
    >
      <BouncehouseLoader />
    </section>
    <div>
      <base-button
        @click.native="checkout()"
        class="bg-black text-white h-12 w-48 my-10"
      >
        Create Reservation
      </base-button>
    </div>
  </main>
</template>

<script>
import BouncehouseLoader from "./bouncehouse/BounceHouseLoader.vue";
import { checkout } from "../mixins/Mixins";

export default {
  name: "Home",
  mixins: [checkout],
  components: {
    BouncehouseLoader,
  },
  data() {
    return {
      image: "tropicalslide4.jpg",
    };
  },
};
</script>
<style scoped>
.scroll {
  width: 1000px;
}
.box {
  display: inline-block;
}
</style>