import json
ruta = "trainers.json"

def guardar_trainer(datos):
        with open(ruta, "w") as file:
            json.dump(datos,file, indent=4)
        print("Datos guardados exitosamente!!")
        print("**************************************************")


def cargar_trainer():
    try:
        with open(ruta, "r") as leer:
            datos=json.loads(leer.read())
            return datos
    except FileNotFoundError:
        
        print("**************************************************")
        return {"Trainers" : {}
    }

print(cargar_trainer())
