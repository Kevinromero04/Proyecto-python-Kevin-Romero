import json
ruta = "rutas_nuevas.json"

def guardar_ruta(datos):
        with open(ruta, "w") as file:
            json.dump(datos,file, indent=4)
        print("Datos guardados exitosamente!!")
        print("**************************************************")


def cargar_ruta():
    try:
        with open(ruta, "r") as leer:
            datos=json.load(leer)
            return datos
    except FileNotFoundError:
        print("Error al guardar datos")
        print("**************************************************")
        return {"Rutas" : {}}




def nuv_rut():
    while True:
        try:
            rhlm  = cargar_ruta()
            ruta = input("Por favor coloque el nombre de la nueva ruta: ")
            nuv = {ruta:{}}
            rhlm["Rutas"][ruta] = {}
            guardar_ruta(rhlm)
            print("Ruta creada")
            print("**************************************************")
            break
        except Exception:
            print("porfavor ingrese un dato valido")
        finally:print("**************************************************")
