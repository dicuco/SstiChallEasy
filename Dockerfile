# Usa una imagen base de Python 3.9
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de la aplicación en el contenedor
COPY app.py flag.txt /app/

# Instala Flask y cualquier otra dependencia
RUN pip install flask

# Expone el puerto que utilizará la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
