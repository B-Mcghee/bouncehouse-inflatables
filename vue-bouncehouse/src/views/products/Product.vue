<template>
  <div>
    <div class="text-4xl my-10">
      <h2>{{ product.name }}</h2>
    </div>
    <div class="grid grid-cols-12 container">
      <div class="col-span-6 row-span-2 mx-4 text-justify text-md">
        <p class="">
          Per day:
          <span class="font-bold text-lg">${{ product.price_per_day }}</span>
        </p>
        <p class="">Wet: <span class="font-bold text-lg">Yes</span></p>
        <p class="">
          <span class="font-bold">Descrption</span>
          {{ product.description }}
        </p>
      </div>
      <div class="col-span-6 row-span-2 mx-4">
        <figure>
          <img :src="require(`@/assets/${product.cover_image}`)" />
        </figure>
      </div>
      <div class="col-span-12">
        <div class="bg-black mt-8 h-auto overflow-x-scroll py-8">
          <div class="min-w-max ml-4">
            <div
              v-for="(image, i) in product.images"
              :key="i"
              class="bg-gray-600 mr-4 inline-block"
            >
              <figure class="h-32">
                <router-link to="inflatable">
                  <img class="h-full" :src="require(`@/assets/${image}`)" />
                </router-link>
              </figure>
            </div>
          </div>
        </div>
      </div>
      <div class="mt-4 col-span-12">
        Choose Date:
        <input class="border-2 border-black" type="datetime-local" />
      </div>
      <div class="col-span-12 mt-4">
        <base-button @click.native="checkout()" class="bg-black text-white w-48"
          >Book Now</base-button
        >
      </div>
    </div>
  </div>
</template>

<script>
import BounceHouseLoader from "../bouncehouse/BounceHouseLoader.vue";
import { checkout } from "../../mixins/Mixins";
export default {
  name: "SingleProduct",
  data() {
    return {
      product: "",
      products: [
        {
          name: "Tropical Slide",
          slug: "tropical-slide",
          description:
            "Just add water to this Tropical slide and it will take through the sprinklers to the pool",
          price_per_day: "250",
          cover_image: "images/tropical_slide/tropical_slide_1.jpg",
          images: [
            "images/tropical_slide/tropical_slide_2.jpg",
            "images/tropical_slide/tropical_slide_3.jpg",
            "images/tropical_slide/tropicalslide4.jpg",
            "images/tropical_slide/tropical_slide5.jpg",
          ],
        },
        {
          name: "Blue Lagoon Slide",
          slug: "blue-lagoon-slide",
          description:
            "A medium sized slide. Add Water from the top, and let it fill up at the bottom to turn this slide into a water slide into a pool, and we have ourselves a party!",
          price_per_day: "250",
          cover_image: "images/Blue Lagoon/blue_lagoon_1.jpg",
          images: [
            "images/Blue Lagoon/blue_lagoon_2.jpg",
            "images/Blue Lagoon/blue_lagoon_3.jpg",
            "images/Blue Lagoon/blue_lagoon_4.jpg",
            "images/Blue Lagoon/blue_lagoon_5.jpg",
          ],
        },
      ],
    };
  },
  mixins: [checkout],
  components: {
    BounceHouseLoader,
  },
  created: function () {
    this.product = this.products.filter(
      (x) => x.slug == this.$route.params.slug
    )[0];
    // this.product.cover_image = "@/assets/" + this.product.cover_image;
  },
};
</script>

<style>
</style>