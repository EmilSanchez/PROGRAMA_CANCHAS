from os import system; system("cls")
import excepciones_time
arbitros=["Emil Sanchez","Daniel Ortiz","Albeiro San Juan","Santiago Sanchez","Andres beltran"]

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
        print("|    4.  --   ELIMINAR ARBITRO                         |")
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
                print(f"\nSe ha finalizado la consulta del árbitro")
            else:
                print(mensaje)
            input("Presione enter --> ")   
        elif opcion==2:
            registrar_arbitro()
        elif opcion==3:
            eliminar_arbitro()
        elif opcion==2:
            nombre_arbitro=registrar_arbitro()
            print(f"Se ha finalizado el registro del árbitro {nombre_arbitro}")
        elif opcion==4:
            break
        else:
            excepciones_time.errores()
            

def consultar_arbitro():
    #validar existencia de árbitro
    if len(arbitros)==0:
        return False,"NO HAY ÁRBITROS REGISTRADOS"
    else:
        #Buscar al árbitro
        consulta = input("Ingrese el nombre completo  del árbitro que desea buscar --> ").title()
        excepciones_time.tiempo("Consultando árbitro ...","RESULTADOS:");system("cls")
        contador=0
        for i in arbitros:
            #Verificar el nombre
            if consulta == i :
                print(f"Árbitro: {consulta} ")
                contador+=1
                return True,i
        else:
            return False,"NO HAY ÁRBITROS REGISTRADOS CON ESE NOMBRE"

            
def registrar_arbitro():
    datos_cliente=[];system("cls")
    print("\n          REGISTRAR ARBITRO           ")
    #pedir nombre
    nombre=input("\nIngrese el nombre y apellido del árbitro --> ").title()

    #Guardar nombre
    arbitros.append(nombre)
    excepciones_time.tiempo("Registrando árbitro ...","Árbitro registrado")
    return nombre          

def eliminar_arbitro():

    #buscar árbitro
    existencia, mensaje_arbitros=consultar_arbitro()
    if existencia:
        arbitros.remove(mensaje_arbitros)#eliminar
        excepciones_time.tiempo("Eliminando árbitro ...","árbitro eliminado ")
    else:
        print(f"{mensaje_arbitros}")
        input("Presione enter")

