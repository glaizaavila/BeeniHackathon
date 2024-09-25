import { createRouter, createWebHistory } from 'vue-router'
import FormView from '@/views/CandidateCreate.vue'
import ListView from '@/views/CandidateView.vue'
import HomeView from '@/views/HomeView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/list',
      name: 'candidateList',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: ListView
    },
    {
      path: '/create',
      name: 'candidateCreate',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: FormView

    }
  ]
})

export default router
