<template>
  <div class="bg-black mt-8 h-auto overflow-x-scroll py-8">
    <div class="min-w-max ml-4">
      <div
        v-for="(product, i) in products"
        :key="i"
        class="bg-gray-600 mr-4 inline-block"
      >
        <figure class="h-32">
          <router-link
            :to="{ name: 'SingleProduct', params: { slug: product.slug } }"
          >
            <img
              class="h-full"
              :src="require(`@/assets/${product.cover_image}`)"
            />
          </router-link>
        </figure>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: { images: [] },
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
      image: "images/tropical_slide/tropical_slide_2.jpg",
    };
  },
};
</script>

<style>
</style>