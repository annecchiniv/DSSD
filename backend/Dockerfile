# Usa una imagen base de Python
ARG PYTHON_VERSION=3.10
FROM python:${PYTHON_VERSION}-slim as backend

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr.
ENV PYTHONUNBUFFERED=1

# Crea un directorio de trabajo
WORKDIR /app

# Crea un usuario no privilegiado para ejecutar la aplicación
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Copia los archivos de requisitos del backend
COPY backend/requirements.txt ./requirements.txt

# Instala las dependencias necesarias
RUN apt-get update && apt-get install -y \
    build-essential \
    libmariadb-dev \
   
