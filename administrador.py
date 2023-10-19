from os import system;system("cls")
import control_usuario
import control_clientes
import control_arbitros
import control_promocion
import control_reportes
import excepciones_time
import control_reservas

#para la promocion activa
#para que de color a las letras
RED = '\033[31m'
WHITE = '\033[37m'

user = "didier"
password= "2023"

def validar_admin():
    while True:
        system("cls")
        print("\nBIENVENIDO  ADMINISTRADOR")
        usuario = input("\nIngrese el nombre de usuario --> ")
        contraseña = input("Ingrese la contraseña --> ")
        
        #Validar usuario y contraseña
        if usuario == user:
            if password == contraseña:
                excepciones_time.tiempo("Ingresando al sistema ...","Ingreso exitoso")
                menu_administrador()
                break
            else:
                print(RED,"")
                print("La contraseña es incorrecta...")
                print(WHITE,"")
                input("Presione Enter para intentarlo nuevamente.. --> ")
                system("cls")
                continue                
        else:
            print(RED,"")
            print("El nombre de usuario es incorrecto...")
            print(WHITE,"")
            input("Presione Enter para intentarlo nuevamente.. --> ")
            system("cls")
            continue

def menu_administrador():
    while True: 
        system("cls");print("=" * 44)
        print("| ADMINISTRACION DE CANCHAS DEPORTIVAS SAS |")
        print("=" * 44)
        print("|    1.  --   CONTROL DE USUARIOS          |")
        print("|    2.  --   CONTROL DE CLIENTES          |")
        print("|    3.  --   CONTROL DE RESERVAS          |")
        print("|    4.  --   CONTROL DE ARBITROS          |")
        print("|    5.  --   CONTROL DE PROMOCIONES       |")
        print("|    6.  --   CONTROL DE REPORTES          |")
        print("|    7.  --   SALIR                        |")
        print("=" * 44); print("")
            
        try:
            opcion = int(input("Ingrese la opcion a ejecutar --> "))         
        except:
            excepciones_time.excepciones()
            continue    
        
        if opcion == 1:
            control_usuario.iniciocont_usuario()
        elif opcion == 2:
            control_clientes.menu_clientes()
        elif opcion == 3:
            control_reservas.disponibilidad_cliente()
        elif opcion == 4:
            control_arbitros.menu_arbitros()
        elif opcion == 5:
            control_promocion.menu_promociones()
        elif opcion == 6:
            control_reportes.inico_reporte()
        elif opcion == 7:
            print("\nGracias por visitarnos!")
            break 
        else:
            print("\nIngrese una opción valida")
    

