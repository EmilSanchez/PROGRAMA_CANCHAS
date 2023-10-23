from os import system;system("cls")
import excepciones_time
import control_reservas
import datetime

#para que de color a las letras
RED = '\033[31m'
WHITE = '\033[37m'

def inico_reporte():
    while True:
        system("cls")
        print("=" * 56)
        print("|    CONTROL DE REPORTES DE CANCHAS DEPORTIVAS SAS    |")
        print("=" * 56)
        print("|    1.  --  CONSULTAR  CANCHAS RESERVADAS POR DÍA    |")
        print("|    2.  --  TOTAL DINERO CAJA                        |")
        print("|    3.  --  SALIR                                    |")
        print("=" * 56);print("")

        try:
            opcion = int(input("Ingrese la opcion a ejecutar --> "))   
        except:
            excepciones_time.excepciones()
            continue    

        if opcion==1:
            consultar_canchas()
        elif opcion==2:
            dinero_caja()
        elif opcion==3:
            break
        else:
            excepciones_time.errores()
    
def  consultar_canchas():
    
    #validar reservas
    if len(control_reservas.total_reservas)==0:
        print("\nNO HAY CANCHAS RESERVADAS ")
        input("Presione enter --> ")

    else:
        while True:
            total_reservadas_dia=0
            try:
                system("cls")
                print("     CONSULTAR  CANCHAS RESERVADAS POR DÍA       ")
                fecha_cancha_str=input("\nIngrese la fecha   (día-mes-año)  --> ")
                fecha_cancha=datetime.datetime.strptime(fecha_cancha_str,"%d-%m-%Y")

                #total  canchas por día
                for i in control_reservas.total_reservas:
                    if  fecha_cancha.date() == i[1].date():
                        total_reservadas_dia+=1

                if total_reservadas_dia>=1:
                    excepciones_time.tiempo("Consultando las canchas ...","Resultados");system("cls")
                    print("\n     CANCHAS RESERVADAS POR DÍA      ")
                    print(f"\nFecha: {fecha_cancha.date()}\t  Total canchas reservadas: {total_reservadas_dia}\n")
                    for i in control_reservas.total_reservas:
                        if  fecha_cancha.date() == i[1].date():
                            print(f"Cliente: {i[0]} \t Cancha: {i[3]} \t Costo total: {i[5]}")
                    input("\nPresione enter -->")
                    break
                else:
                    print("\nNo hay canchas reservadas ese día")
                    input("Presione enter --> ")
                    break
            except:
                system("cls")
                print(RED,"\nINGRESASTE MAL LA FECHA, INGRESALA ASÍ DÍA-MES-AÑO ",WHITE)

def dinero_caja():

    #validar reservas
    if len(control_reservas.total_reservas)==0:
        print("NO HAY DINERO EN CAJA ")
        input("Presione enter --> ")

    else:
        total=0
        for i in control_reservas.total_reservas:

            #el dinero de la reserva es i[5]
            total+=i[5]
        excepciones_time.tiempo("Revisando  caja ...","Resultados de la caja");system("cls")
        print(f"\nTOTAL DINERO DE CAJA:  $ {total}")
        input("Presione enter")



