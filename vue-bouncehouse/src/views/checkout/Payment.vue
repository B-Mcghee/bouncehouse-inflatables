<template>
  <div>
    <base-title>
      <h2>Payment</h2>
    </base-title>
    <div class="text-center">
      <form class="bg-blue-200 max-w-xs mx-auto py-4 rounded-md">
        <base-input>
          <label for="card-number">Card Number:</label>
          <input-box placeholder="Card Number" />
        </base-input>
        <base-input>
          <label for="reserve-date">Expire Date:</label>
          <input-box :mode="'date'" placeholder="mm-yy" />
        </base-input>
        <base-input>
          <label for="cvv">CVV:</label>
          <input-box maxlength="3" size="3" />
        </base-input>
        <base-input>
          <label for="cardholder-name">Cardholder Name:</label>
          <input-box placeholder="Cardholder Name" />
        </base-input>
      </form>
      <div class="mt-4">
        <router-link to="/checkout/payment"
          ><base-button class="mx-2"
            >Pay Secure &#8594;</base-button
          ></router-link
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