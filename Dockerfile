FROM python:3.11-slim

# Evita que Python almacene en búfer la salida estándar (para ver los logs en tiempo real)
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copiar el proyecto al contenedor
COPY . /app/

# Por defecto ejecuta el primer ejemplo
CMD ["python", "1_secuencial/main.py"]
