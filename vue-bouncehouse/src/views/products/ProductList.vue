<template>
  <div>
    <div class="text-4xl my-10">
      <h2>All Inflatables</h2>
    </div>
    <Toolbar />
    <div class="h-full">
      <div class="overflow-y-scroll">
        <div
          v-for="(product, i) in products"
          :key="i"
          class="
            bg-gray-600
            max-h-32
            w-full
            border-2 border-black
            overflow-y-hidden
          "
        >
          <router-link
            :to="{ name: 'SingleProduct', params: { slug: product.slug } }"
          >
            <img :src="require(`@/assets/${product.cover_image}`)" />
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Toolbar from "@/layouts/Toolbar";
export default {
  components: {
    Toolbar,
  },
  data() {
    return {
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
        {
          name: "Tropical Slide",
          slug: "tropical-slide",
          description:
            "A big tropical themed slide that you can add water on the slide that will take you through the sprinkler foutains to the end pool",
          price_per_day: "250",
          cover_image: "images/tropical_slide/tropical_slide_2.jpg",
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
          cover_image: "images/Blue Lagoon/blue_lagoon_2.jpg",
          images: [
            "images/Blue Lagoon/blue_lagoon_2.jpg",
            "images/Blue Lagoon/blue_lagoon_3.jpg",
            "images/Blue Lagoon/blue_lagoon_4.jpg",
            "images/Blue Lagoon/blue_lagoon_5.jpg",
          ],
        },
        {
          name: "Tropical Slide",
          slug: "tropical-slide",
          description:
            "A big tropical themed slide that you can add water on the slide that will take you through the sprinkler foutains to the end pool",
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
          cover_image: "images/Blue Lagoon/blue_lagoon_3.jpg",
          images: [
            "images/Blue Lagoon/blue_lagoon_2.jpg",
            "images/Blue Lagoon/blue_lagoon_3.jpg",
            "images/Blue Lagoon/blue_lagoon_4.jpg",
            "images/Blue Lagoon/blue_lagoon_5.jpg",
          ],
        },
        {
          name: "Tropical Slide",
          slug: "tropical-slide",
          description:
            "A big tropical themed slide that you can add water on the slide that will take you through the sprinkler foutains to the end pool",
          price_per_day: "250",
          cover_image: "images/tropical_slide/tropical_slide_3.jpg",
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
};
</script>

<style>
</style>