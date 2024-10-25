# Usar una imagen base de Python
FROM python:3.13

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de requerimientos
COPY backend/requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente de la aplicación
COPY backend/ .

# Construir el frontend
WORKDIR /app/frontend
COPY frontend/package.json .
COPY frontend/package-lock.json .
RUN npm install
RUN npm run build

# Exponer el puerto en el que la aplicación estará corriendo
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
