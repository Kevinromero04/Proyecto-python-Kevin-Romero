import json
ruta = "registros.json"

def guardar_usuario(datos):
        with open(ruta, "w") as file:
            json.dump(datos,file, indent=4)
        print("Datos guardados exitosamente!!")
        print("**************************************************")


def cargar_ususario():
    try:
        with open(ruta, "r") as leer:
            datos=json.load(leer)
            return datos
    except FileNotFoundError:
        print("Error al guardar datos")
        print("**************************************************")
        return {"registrados":{ }}
