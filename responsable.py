from os import system;system("cls")
import excepciones_time
import control_usuario
import control_clientes
import control_reservas
#para que de color a las letras
RED = '\033[31m'
WHITE = '\033[37m'

#user_responsables[["Luisa Araque","1065871433","luisa22"]]

def validar_respon():
    
    if len(control_usuario.users_responsables)==0:
        print("No hay responsables registrados, el administrador debe registrar su cuenta")
        input("Presione enter -->")
    else:
        while True:
            system("cls");salir=False
            print("\n       BIENVENIDO  RESPONSABLE")
            #Validar cuenta de responsable
            usuario = input("\nIngrese su identificación --> ")
            contraseña = input("Ingrese la contraseña --> ")
            for i in control_usuario.users_responsables:
                if usuario==i[1] and contraseña == i[2]:
                    excepciones_time.tiempo("Ingresando al sistema ...","Ingreso exitoso")
                    menu_responsable()
                    salir=True
            if salir:
                break       
            else:
                    print(RED,"")
                    print("Usuario o contraseña incorrecta...")
                    print(WHITE,"")
                    input("Presione Enter para intentarlo nuevamente.. --> ")
                    system("cls")
                    continue      

def menu_responsable():
    while True: 
        system("cls")
        print("=" * 44)
        print("|    RESPONSABLE DE CANCHAS DEPORTIVAS SAS |")
        print("=" * 44)
        print("|    1.  --   GESTION DE CLIENTES          |")
        print("|    2.  --   GESTION DE RESERVAS          |")
        print("|    3.  --   SALIR                        |")
        print("=" * 44); print("")

        try:
            opcion = int(input("Ingrese la opcion a ejecutar --> "))         
        except:
            excepciones_time.excepciones()
            continue    

        if opcion == 1:
            control_clientes.menu_clientes()
        elif opcion == 2:
            control_reservas.disponibilidad_cliente()
        elif opcion == 3:
            break 
        else:
            excepciones_time.errores()       
