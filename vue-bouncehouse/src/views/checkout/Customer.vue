<template>
  <div>
    <base-title>
      <h2>Customer</h2>
    </base-title>
    <div class="text-center">
      <form class="bg-blue-200 max-w-xs mx-auto py-4 rounded-md">
        <base-input>
          <label for="inflatable">First name:</label>
          <input-box placeholder="First Name" />
        </base-input>
        <base-input>
          <label for="reserve-date">Last Name:</label>
          <input-box placeholder="Last Name" />
        </base-input>
        <base-input>
          <label for="deposit">Email:</label>
          <input-box placeholder="Email" />
        </base-input>
        <base-input>
          <label for="rentail-price">Phone Number:</label>
          <input-box placeholder="Phone Number" />
        </base-input>
        <base-input>
          <label for="days">Address</label>
          <input-box placeholder="Address" />
        </base-input>
        <base-input>
          <label for="days">City</label>
          <input-box placeholder="City" />
        </base-input>
        <base-input>
          <label for="days">State</label>
          <input-box placeholder="State" />
        </base-input>
      </form>
      <div class="mt-4">
        <router-link to="/checkout/review"
          ><base-button class="mx-2">&#8592; Back</base-button></router-link
        >
        <router-link to="/checkout/payment"
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