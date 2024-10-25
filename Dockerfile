FROM python:3.11

# Instala las dependencias necesarias
RUN apt-get update && apt-get install -y \
    build-essential \
    libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de tu proyecto
COPY . .

# Crea un entorno virtual y activa
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Instala las dependencias de Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exponer el puerto en el que la aplicación escuchará
EXPOSE 8000

# Comando por defecto para ejecutar la aplicación
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
