import json
from menus import menu_coor
import aprobar_denegar as pd
import mostrar_usuarios as mostra
import modificar_nota_cordi as notas
import crea_ruta
import carga_Coor as mm
import asignar_ruta_grupo
def wel_coor ():
    ss = mm.cargar_coor()
    clave1 = input("Digite la clave: ").lower()
    if clave1 in ss["Coordinador"]:
        usuario = ss["Coordinador"][clave1]["usuario"]
        print("Bienvenido ", usuario)
        print("**************************************************")
        while True:
            menu_coor()
            opc_cor = int(input("Seleccione una opcion"))
            if opc_cor == 1:
                pd.aprobar()
                pd.mover_usuario_aprobado()
                
            elif opc_cor ==2:
                mostra.mos_ins()
                
            elif opc_cor ==3:
                mostra.mos_trains()
                
            elif opc_cor ==4:
                asignar_ruta_grupo.rhlm()
                
            elif opc_cor ==5:
                notas.modi_cordi()
                
            elif opc_cor ==6:
                crea_ruta.nuv_rut()
                
            elif opc_cor ==7:
                mostra.mos_camp()
            elif opc_cor ==8:
                print("Saliendo...")
                break
            else:
                print("Numero incorrecto")
                break
                
    else:
        
        print("Clave invalida")
        print("**************************************************")


