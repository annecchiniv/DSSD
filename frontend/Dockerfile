# Usa una imagen base de Node.js
FROM node:16 as frontend

# Crea un directorio de trabajo
WORKDIR /app

# Copia los archivos de requisitos del frontend
COPY requirements.txt ./requirements.txt

# Instala las dependencias del frontend
RUN npm install

# Copia todo el código fuente del frontend en el contenedor
COPY . .

# Construye la aplicación del frontend (ajusta este comando según sea necesario)
RUN npm run build

# Exponer el puerto en el que la aplicación del frontend escuchará
EXPOSE 3000

# Comando para ejecutar la aplicación del frontend
CMD ["npm", "start"]
