# 📄 PDF Tools - Local

Herramienta web local para manipulación de archivos PDF construida con Python y Streamlit. Procesa todos tus documentos de forma segura sin enviarlos a servidores externos, manteniendo tu privacidad al 100%.

## 🌟 Características

- **🔗 Fusionar PDFs**: Combina múltiples archivos PDF en un solo documento
- **✂️ Dividir PDF**: Extrae páginas específicas o rangos de páginas
- **📄 PDF a Word**: Convierte archivos PDF a formato DOCX editable
- **🔄 Rotar Páginas**: Aplica rotación de 90°, 180° o 270° a tus documentos
- **🗑️ Eliminar Páginas**: Remueve páginas específicas de tus PDFs
- **🔒 100% Local**: Sin conexión a servicios externos - tus archivos nunca salen de tu infraestructura

## 📋 Requisitos Previos

- Docker y Docker Compose instalados
- Puerto 8501 disponible en tu máquina

## 📁 Estructura del Proyecto

```
pdf-tools/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── app.py
└── README.md
```
```


## 🚀 Instalación y Uso

### Opción 1: Con Docker Compose (Recomendado)

1. **Clonar o crear el proyecto**:
mkdir pdf-tools
cd pdf-tools

2. **Crear los archivos necesarios** (Dockerfile, docker-compose.yml, requirements.txt, app.py)

3. **Construir y ejecutar**:
docker-compose up --build -d

4. **Acceder a la aplicación**:
http://localhost:8501


### Opción 2: Con Docker directamente

Construir la imagen
docker build -t pdf-tools-local .

Ejecutar el contenedor
docker run -d --name pdf-tools -p 8501:8501 pdf-tools-local


## 📦 Archivos de Configuración

### Dockerfile

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]


### docker-compose.yml

version: '3.8'

services:
pdf-tools:
build: .
ports:
- "8501:8501"
restart: unless-stopped


### requirements.txt

streamlit
pypdf
pdf2docx


## 🎯 Funcionalidades Detalladas

### Fusionar PDFs
- Sube múltiples archivos PDF
- Se fusionan en el orden en que se cargan
- Descarga un único archivo consolidado

### Dividir PDF
- Extrae páginas por rango (ej: páginas 1-5)
- Selecciona páginas individuales (ej: 2,4,6)
- Genera un nuevo PDF con las páginas seleccionadas

### PDF a Word
- Convierte PDFs a formato DOCX
- Mantiene la estructura del documento
- Permite edición posterior en Microsoft Word o LibreOffice

### Rotar Páginas
- Selecciona ángulo de rotación: 90°, 180°, 270°
- Aplica rotación a todas las páginas o solo a páginas específicas
- Mantiene la calidad del documento

### Eliminar Páginas
- Especifica las páginas a eliminar separadas por comas
- Genera un nuevo PDF sin las páginas seleccionadas
- Útil para remover páginas en blanco o contenido no deseado

## 🛠️ Tecnologías Utilizadas

- **Python 3.11**: Lenguaje de programación principal
- **Streamlit**: Framework para la interfaz web
- **pypdf**: Librería para manipulación de PDFs
- **pdf2docx**: Conversión de PDF a Word
- **Docker**: Containerización y despliegue

## 🔧 Comandos Útiles

### Ver logs del contenedor
docker-compose logs -f

### Detener el servicio
docker-compose down

### Reiniciar el servicio
docker-compose restart

### Reconstruir la imagen
docker-compose up --build -d

### Eliminar contenedor e imagen
docker-compose down
docker rmi pdf-tools-local


## 🐛 Solución de Problemas

### El puerto 8501 está ocupado
Modifica el puerto en `docker-compose.yml`:
ports:

"8502:8501" # Cambia 8502 por el puerto que prefieras


### Error de permisos en archivos temporales
El contenedor maneja automáticamente los archivos temporales. Si experimentas problemas, reinicia el contenedor:
docker-compose restart


### La aplicación no carga
Verifica que el contenedor esté ejecutándose:
docker ps

Si no aparece, revisa los logs:
docker-compose logs


## 🔐 Seguridad y Privacidad

- **Procesamiento Local**: Todos los archivos se procesan dentro del contenedor Docker
- **Sin almacenamiento permanente**: Los archivos temporales se eliminan después del procesamiento
- **Sin conexiones externas**: No se envían datos a servicios de terceros
- **Aislamiento**: Docker proporciona aislamiento del sistema host

## 📝 Notas Adicionales

- Los archivos procesados no se guardan en el servidor
- Cada operación es independiente y no afecta archivos previos
- La aplicación puede procesar PDFs de cualquier tamaño (sujeto a recursos del sistema)
- Compatible con Windows, macOS y Linux mediante Docker

## 🤝 Contribuciones

Este proyecto fue diseñado para uso personal y privacidad máxima. Siéntete libre de modificarlo según tus necesidades.

## 📄 Licencia

Proyecto de código abierto para uso personal y educativo.

---

**Desarrollado para mantener tus documentos privados y seguros**
