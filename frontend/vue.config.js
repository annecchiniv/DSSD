const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  publicPath: process.env.NODE_ENV === 'production' ? '/' : '/',
  devServer: {
    allowedHosts: 'all', // Permite todos los hosts
    host: '0.0.0.0', // Escucha en todas las interfaces
    port: process.env.PORT || 8080, // Asegúrate de usar el puerto correcto
    https: true, // Habilita HTTPS
    client: {
      webSocketURL: 'wss://0.0.0.0:8080/ws', // Cambia el URL de WebSocket a WSS
    },
  },
});