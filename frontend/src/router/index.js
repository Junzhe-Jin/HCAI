import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from '../views/LoginPage.vue'
import DashboardPage from '../views/DashboardPage.vue'

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: LoginPage },
  { path: '/dashboard', component: DashboardPage }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const apiKey = sessionStorage.getItem("openai_api_key")  // 这里改成 sessionStorage
  if (to.path !== '/login' && !apiKey) {
    next('/login')
  } else {
    next()
  }
})

export default router
