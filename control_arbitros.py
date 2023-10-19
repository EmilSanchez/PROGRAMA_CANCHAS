from os import system; system("cls")
import excepciones_time
arbitros=["Emil Sanchez","Daniel Ortiz","Albeiro San Juan","Santiago Sanchez","S"]

def menu_arbitros():
    while True:
        system("cls")
        #Menu de árbitros
        system("cls")
        print("=" * 56)
        print("|    CONTROL DE ARBITROS DE CANCHAS DEPORTIVAS SAS     |")
        print("=" * 56)
        print("|    1.  --   CONSULTAR ARBITRO                        |")
        print("|    2.  --   REGISTRAR ARBITRO                        |")
        print("|    3.  --   SALIR                                    |")
        print("=" * 56);print("")

        try:
            opcion = int(input("Ingrese la opcion a ejecutar --> "))   
        except:
            excepciones_time.excepciones()
            continue    

        if opcion==1:
            existencia_arbitro,mensaje=consultar_arbitro()
            if existencia_arbitro==True:
                print(f"Se ha finalizado la consulta del arbitro {mensaje}")
            else:
                print(mensaje)
            input("Presione enter --> ")
        elif opcion==2:
            registrar_arbitro()
        elif opcion==3:
            break
        else:
            excepciones_time.errores()
            

def consultar_arbitro():
    #validar existencia de árbitro
    if len(arbitros)==0:
        return False,"NO HAY ÁRBITROS REGISTRADOS"
    else:
        #Buscar al árbitro
        consulta = input("Ingrese el nombre y apellido del árbitro que desea buscar --> ")
        excepciones_time.tiempo("Consultando árbitro ...","RESULTADOS:");system("cls")
        contador=0
        for i in arbitros:
            if consulta == i :
                print(f"Árbitro: {i} ")
                input("Presione Enter.. --> ")
                contador+=1
                break
        else:
            print("No hay árbitros con este nombre")
            
def registrar_arbitro():
    datos_cliente=[];system("cls")
    print("\n          REGISTRAR ARBITRO           ")
    #pedir datos
    nombre=input("\nIngrese el nombre y apellido del árbitro --> ").title()

    #Guardar datos
    arbitros.append(nombre)
    excepciones_time.tiempo("Registrando árbitro ...","Árbitro registrado")
    return nombre          