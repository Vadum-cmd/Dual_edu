import { createApp } from 'vue'
import App from './App.vue'
import router from "@/components/router";
import {FontAwesomeIcon} from "@/components/plugins/fontAwesome";
import VueAwesomePaginate from "vue-awesome-paginate";

// import the necessary css file
import "vue-awesome-paginate/dist/style.css";
const app = createApp(App).component("font-awesome-icon", FontAwesomeIcon);
app.use(router)
app.mount('#app')
app.use(VueAwesomePaginate)