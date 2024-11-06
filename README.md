
# Proyecto de Clima con Flask

Este proyecto es una aplicación web en Python que obtiene datos de clima en tiempo real mediante una API y los muestra de manera amigable usando Flask.

## Características

- Obtiene datos de clima en tiempo real desde la API de OpenWeatherMap.
- Muestra la información del clima, incluyendo temperatura, humedad y descripción, en una interfaz web.
- Organiza los datos de una manera clara y accesible con la ayuda de Python y Flask.

## Requisitos previos

- Python 3.x instalado en tu sistema.
- Una clave API de OpenWeatherMap. Puedes obtener una creando una cuenta gratuita en [OpenWeatherMap](https://openweathermap.org/).

## Instalación

1. **Clona este repositorio** o descarga el código fuente:

   ```bash
   git clone https://github.com/ramiroec/clima-python.git
   cd proyecto-clima
   ```

2. **Instala las dependencias** usando el archivo `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configura la clave API**:

   Crea un archivo `.env` en la raíz del proyecto y agrega tu clave de OpenWeatherMap API en el siguiente formato:

   ```plaintext
   WEATHER_API_KEY='tu_api_key'
   ```

   Reemplaza `'tu_api_key'` con tu clave API de OpenWeatherMap.

## Ejecución del Proyecto

Para iniciar la aplicación, ejecuta el siguiente comando en la terminal:

```bash
python app.py
```

Esto iniciará el servidor en `http://127.0.0.1:5000/`. Abre tu navegador y ve a esa dirección para ver la aplicación en funcionamiento.

## Uso

- **Inicio**: Al ingresar en la dirección del servidor local, podrás ver el formulario para ingresar una ciudad.
- **Buscar Clima**: Ingresa el nombre de una ciudad y envía el formulario. La aplicación mostrará la información del clima para la ciudad ingresada.

## Tecnologías Usadas

- **Python**
- **Flask** - para la creación del servidor web.
- **requests** - para hacer las solicitudes HTTP a la API de clima.
- **HTML/CSS** - para el diseño de la interfaz web.

## Dependencias

Las dependencias del proyecto están en el archivo `requirements.txt`. Las principales son:

- Flask
- requests

## Créditos

Este proyecto fue desarrollado con la guía de OpenAI ChatGPT para aprender sobre el uso de APIs y el desarrollo web en Python.

---

¡Esperamos que disfrutes del proyecto!
