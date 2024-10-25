import { createRouter, createWebHistory } from "vue-router";
import store from './store/index';
import Home from './components/Home';
import Recolectores from './components/Recolectores/Index';
import Recolector from './components/Recolectores/Show';
import Login from './components/Login';
import Register from './components/RegisterForm.vue';
import FormularioPlan from './components/Materiales/FormularioPlan.vue';
import Layout from './components/Layout.vue';
import Ordenes from './components/Ordenes/Show.vue';
import CrearOrden from '@/components/Ordenes/Create.vue';  
import Depositos from './components/Depositos/Show.vue';
import CrearDeposito from './components/Depositos/Create.vue';

const routes = [
    { 
        path: "/", 
        component: Layout,  // Envuelve todas las páginas en el Layout
        meta: { requiresAuth: true },  // Requiere autenticación
        children: [
            {
                path: '',
                name: 'Home-Component',
                component: Home
            },
            {
                path: "materiales/material/new", 
                name: 'Formulario-Material', 
                component: FormularioPlan
            },
            {
                path: "recolectores/recolector/:id", 
                name: 'Recolector-Show', 
                component: Recolector
            },
            {
                path: "recolectores/recolectores", 
                name: 'Recolectores-Show', 
                component: Recolectores
            },
            {
                path: '/ordenes',   
                name: 'Ordenes',
                component: Ordenes
              },
              {
                path: '/ordenes/nueva',
                name: 'CrearOrden',
                component: CrearOrden  
              },
              {
                path: '/depositos',
                name: 'Depositos',
                component: Depositos  
              },
              {
                path: '/deposito/nueva',
                name: 'CrearDeposito',
                component: CrearDeposito  
              }
        ]
    },
    { 
        path: "/iniciar-sesion", 
        name: 'Login-Component', 
        component: Login,
        beforeEnter: (to, from, next) => {
            if (store.getters['auth/isLoggedIn']) {
                next('/');
            } else {
                next();
            }
        }
    },
    { 
        path: "/registrar", 
        name: 'Register', 
        component: Register 
    },
];

const Router = createRouter({
    history: createWebHistory(),
    routes
});


Router.beforeEach((to, from, next) => {
    const token = localStorage.getItem('token');
    if (to.meta.requiresAuth && !token) {
        next('/iniciar-sesion');
    } else {
        next();
    }
});


export default Router;