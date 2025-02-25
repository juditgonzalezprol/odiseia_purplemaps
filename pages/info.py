from serpapi import GoogleSearch
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# 1. Solicitar la ubicación del usuario
user_location_input = input("Ingrese su ubicación: ")

# 2. Convertir la dirección ingresada a coordenadas (latitud y longitud)
geolocator = Nominatim(user_agent="mi_app")
user_location = geolocator.geocode(user_location_input)
if not user_location:
    print("No se pudo determinar la ubicación ingresada.")
    exit(1)
user_coords = (user_location.latitude, user_location.longitude)

# 3. Definir una lista de puntos violetas con sus direcciones y coordenadas (ejemplo)
violeta_points = [
    {
        "name": "Punto Violeta 1",
        "address": "Calle Falsa 123, Ciudad, País",
        "coords": (40.4168, -3.7038)  # Ejemplo: coordenadas de Madrid
    },
    {
        "name": "Punto Violeta 2",
        "address": "Avenida Siempre Viva 742, Ciudad, País",
        "coords": (40.4188, -3.7048)
    },
    {
        "name": "Punto Violeta 3",
        "address": "Calle Real 456, Ciudad, País",
        "coords": (40.4160, -3.7010)
    }
]

# 4. Calcular el punto violeta más cercano utilizando la distancia geodésica
closest_point = None
min_distance = float('inf')
for point in violeta_points:
    distance = geodesic(user_coords, point["coords"]).meters
    if distance < min_distance:
        min_distance = distance
        closest_point = point

if closest_point:
    print(f"El punto violeta más cercano es: {closest_point['name']} ({closest_point['address']})")
    
    # 5. Solicitar la ruta desde la ubicación del usuario hasta el punto violeta más cercano usando SerpApi
    params = {
      "engine": "google_maps_directions",
      "start_addr": user_location_input,
      "end_addr": closest_point["address"],
      "api_key": "secret_api_key"  # Reemplaza con tu API key real
    }
    
    search = GoogleSearch(params)
    results = search.get_dict()
    
    # Se asume que la clave "directions" contiene la ruta formateada o los pasos
    directions = results.get("directions")
    if directions:
        print("Ruta generada:")
        print(directions)
    else:
        print("No se pudo obtener la ruta mediante la API.")
else:
    print("No se encontró ningún punto violeta cercano.")
