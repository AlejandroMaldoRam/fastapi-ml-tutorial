# Programa para usar nuestra API desde otro programa
import requests
import json

if __name__ == '__main__':
    # Definimos los casos a probar
    data = [{"Age": 5, "Sex": "male", "Embarked": "S"}, {"Age": 15, "Sex": "female", "Embarked": "Q"}]
    #data = [{"Age": 85, "Sex": "male", "Embarked": "S"}]

    #json_data = json.dump(data)

    # Mandamo el mensaje al API
    r = requests.post("http://127.0.0.1:8000/predict", json=data)

    print("Respuesta cruda: ", r.json())