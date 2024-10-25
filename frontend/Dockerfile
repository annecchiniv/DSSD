# Usa la imagen de Node.js
FROM node:16

# Define el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo package.json y package-lock.json al contenedor
COPY package.json package-lock.json ./

# Instala las dependencias
RUN npm install

# Copia el resto del código fuente del frontend
COPY . .

# Expone el puerto en el que corre la aplicación (ajusta el puerto según tu configuración)
EXPOSE 8080

# Comando para ejecutar la aplicación
CMD ["npm", "start"]
