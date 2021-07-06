<template>
  <div>
    <base-title>
      <h2>Order</h2>
    </base-title>
    <div class="text-center">
      <form class="bg-blue-200 max-w-xs mx-auto py-4 rounded-md">
        <base-input>
          <label for="inflatable">Inflatable:</label>
          <select
            class="
              w-48
              border-2 border-gray-200
              focus:ring-2 focus:ring-gray-600
              focus:outline-none
              bg-white
              rounded-lg
            "
          >
            <option v-for="(n, i) in 7" :key="i">{{ n }}</option>
          </select>
        </base-input>
        <base-input>
          <label for="reserve-date">Reserved Date:</label>
          <input-box
            class="bg-white"
            :mode="'datetime-local'"
            placeholder="08/21/2021 4:00pm"
          />
        </base-input>
        <base-input>
          <label for="deposit">Security Deposit:</label>
          <input-box type="text" readonly placeholder="$100" />
        </base-input>
        <base-input>
          <label for="rentail-price">Rental Price Per day:</label>
          <input-box type="text" readonly placeholder="$225" />
        </base-input>
        <base-input>
          <label for="days">Days:</label>
          <input-box type="text" readonly placeholder="1" />
        </base-input>
        <base-title>
          <p>Due Now: $225</p>
        </base-title>
      </form>
      <div class="mt-4">
        <base-button class="mx-2">&#8592; Back</base-button>
        <router-link to="/checkout/customer"
          ><base-button class="mx-2">Next &#8594;</base-button></router-link
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style>
</style>