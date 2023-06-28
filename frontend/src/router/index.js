import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Usuariosview from '../views/Usuarios/View.vue'
import UsuariosCrear from '../views/Usuarios/Agregar.vue'
import UsuariosEditar from '../views/Usuarios/Editar.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/usuarios',
      name: 'usuarios',
      component: Usuariosview
    },
    {
      path: '/usuarios/agregar',
      name: 'usuariosAgregar',
      component: UsuariosCrear
    },
    {
      path: '/usuarios/:id',
      name: 'usuariosEditar',
      component: UsuariosEditar
    }
    
  ]
})

export default router
