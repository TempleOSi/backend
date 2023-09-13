# Usamos la imagen base de Python 3.8
FROM python:3.9

# Establecemos el directorio de trabajo en /app
WORKDIR /app

# Copiamos el archivo de requisitos a la imagen
COPY requirements.txt .

# Instalamos las dependencias del proyecto
RUN pip install -r requirements.txt

# Copiamos todos los archivos al directorio de trabajo en la imagen
COPY . .

# Copiamos el archivo de configuración db_config.json al directorio de trabajo en la imagen
COPY db_config.json .

# Exponemos el puerto 8080 en el contenedor (ajusta el puerto si es necesario)
EXPOSE 8080

# Ejecutamos tu script de Python cuando se inicie el contenedor
# CMD ["python", "app.py"]
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app