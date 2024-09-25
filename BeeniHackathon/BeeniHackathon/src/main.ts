import './assets/main.css'
import 'bootstrap/dist/css/bootstrap.css'
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle.js'
import Vue3EasyDataTable from 'vue3-easy-data-table'
import 'vue3-easy-data-table/dist/style.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App).use(bootstrap).component('EasyDataTable', Vue3EasyDataTable)

app.use(router)

app.mount('#app')
