# Usa una imagen base de Node.js
FROM node:18 as frontend

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requisitos del frontend
COPY frontend/requirements.txt ./requirements.txt

# Instala las dependencias necesarias (ajusta según tu stack)
RUN npm install

# Copia el código fuente del frontend
COPY frontend/ ./frontend/

# Construye la aplicación
RUN npm run build

# Exponer el puerto en el que la aplicación escuchará (ajusta según el puerto)
EXPOSE 3000

# Comando para ejecutar la aplicación
CMD ["npm", "start"]
