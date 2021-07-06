import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import BaseInput from './components/UI/BaseInput.vue'
import BasePageTitle from './components/UI/BasePageTitle.vue'
import InputBox from './components/UI/InputBox.vue'
import BaseButton from './components/UI/BaseButton.vue'
import './main.css'
import "tailwindcss/tailwind.css"

Vue.config.productionTip = false
Vue.component("base-input",BaseInput);
Vue.component("base-title",BasePageTitle);
Vue.component("input-box",InputBox);
Vue.component("base-button", BaseButton);


new Vue({
  router,
  store,
  render: function (h) { return h(App) }
}).$mount('#app')
