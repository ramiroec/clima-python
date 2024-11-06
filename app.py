from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Configuración inicial
API_KEY = '9310bae179295f6eb70c57737b374771'  # Reemplaza con tu clave de API
ciudad = 'Asuncion, PY'  # Nombre de la ciudad y país
iconos_clima = {
    "clear sky": "☀️", "few clouds": "🌤️", "scattered clouds": "⛅",
    "broken clouds": "🌥️", "shower rain": "🌦️", "rain": "🌧️",
    "thunderstorm": "⛈️", "snow": "❄️", "mist": "🌫️", "overcast clouds": "☁️"
}

def obtener_clima():
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es'
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        datos_clima = respuesta.json()
        
        # Extracción de datos relevantes
        dia = 'Hoy'
        temperatura = datos_clima['main']['temp']
        humedad = datos_clima['main']['humidity']
        velocidad_viento = datos_clima['wind']['speed']
        descripcion = datos_clima['weather'][0]['description']
        probabilidad_lluvia = datos_clima.get('rain', {}).get('1h', 0)
        icono = iconos_clima.get(descripcion, "🌈")

        return {
            "dia": dia, "temperatura": temperatura, "humedad": humedad,
            "velocidad_viento": velocidad_viento, "probabilidad_lluvia": probabilidad_lluvia,
            "descripcion": descripcion, "icono": icono
        }
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

@app.route('/')
def index():
    clima_datos = obtener_clima()
    return render_template("index.html", clima=clima_datos)

if __name__ == '__main__':
    app.run(debug=True)
