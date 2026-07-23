# Usamos una imagen base oficial y ligera
FROM python:3.12-slim

# Evita que Python escriba archivos .pyc y fuerza el stdout inmediato
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Copiamos primero los requerimientos para aprovechar la caché de capas de Docker
COPY requirements.txt .

# Instalamos dependencias sin guardar caché del gestor de paquetes
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código
COPY app/ ./app/

# Exponemos el puerto
EXPOSE 5000

# Usuario no-root por seguridad (Buena práctica que Hadolint revisará)
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Comando de arranque con servidor de producción Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.main:app"]