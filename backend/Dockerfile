# Usa una imagen base de Python
ARG PYTHON_VERSION=3.10
FROM python:${PYTHON_VERSION}-slim as base

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
COPY requirements.txt ./requirements.txt

# Instala las dependencias necesarias
RUN apt-get update && apt-get install -y \
    build-essential \
    libmariadb-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Descarga e instala las dependencias de Python del backend
RUN --mount=type=cache,target=/root/.cache/pip \
    python -m pip install --upgrade pip \
    && python -m pip install -r ./requirements.txt

# Copia el código fuente en el contenedor
COPY . .

# Cambia al usuario no privilegiado
USER appuser

# Exponer el puerto en el que la aplicación escuchará
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
