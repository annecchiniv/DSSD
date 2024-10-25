import { apiService } from '@/api';
import axios from 'axios';

const namespaced = true;

const state = {
    user: null,
    isLoggedIn: false,
    token: null
};

const getters = {
    isLoggedIn: state => state.isLoggedIn,
    user: state => state.user,
    token: state => state.token
};

const actions = {
    async loginUser({ commit }, user) {
        try {
            const response = await apiService.post('/auth/login_jwt', user);
            localStorage.setItem('token', response.data.token);
            localStorage.setItem('user', JSON.stringify(response.data.user));
            commit('setToken', response.data.token);
            commit('setUser', response.data.user);
        } catch (error) {
            console.error('Error en login:', error);
            throw error;
        }
    },
    async fetchUser({ commit }) {
        try {
            const response = await apiService.get('/auth/user_jwt');
            commit('setUser', response.data);
        } catch (error) {
            console.error('Error al obtener usuario:', error);
        }
    },
    async logoutUser({ commit }) {
        try {
            await apiService.get('/auth/logout_jwt');
            commit('clearUser');
        } catch (error) {
            console.error('Error en logout:', error);
        }
    },
    async registerUser(_, user) {
        const response = await axios.post('http://localhost:5000/api/registrar_usuario', user);
        return response.data;
    },
    setToken({ commit }, token) {
        commit('setToken', token);
    }
};

const mutations = {
    setUser(state, user) {
        state.user = user;
    },
    setToken(state, token) {
        state.token = token;
        state.isLoggedIn = true;
        const user = JSON.parse(atob(token.split('.')[1])); // Extraer datos del usuario del token
        state.user = user;
    },
    clearUser(state) {
        state.isLoggedIn = false;
        state.user = null;
        state.token = null;
        localStorage.removeItem('token');
        localStorage.removeItem('user');
    }
};

export default {
    namespaced,
    state,
    getters,
    actions,
    mutations
};