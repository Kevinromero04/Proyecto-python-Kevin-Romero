import json
ruta = "coordinador.json"

def guardar_trainer(datos):
        with open(ruta, "w") as file:
            json.dump(datos,file, indent=4)
        print("Datos guardados exitosamente!!")
        print("**************************************************")


def cargar_coor():
    try:
        with open(ruta, "r") as leer:
            datos=json.loads(leer.read())
            return datos
    except FileNotFoundError:
        print("**************************************************")
        return {"Coordinador" : {} }
    
    
