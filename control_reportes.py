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
        excepciones_time.tiempo("","")
        print("NO HAY CANCHAS RESERVADAS ")
    else:
        while True:
            print("     CANCHAS RESERVADAS POR DÍA      ")

            total_reservadas=0
            try:
                fecha_cancha_str=input("\nIngrese la fecha de la cancha  (años-mes-dia)  --> ")
                fecha_cancha=datetime.datetime.strptime(fecha_cancha_str,"%Y-%m-%d")
                for i in control_reservas.total_reservas:
                    if  fecha_cancha.date() == i[1].date():
                        total_reservadas+=1

                excepciones_time.tiempo("Consultando las canchas ...","Resultados");system("cls")
                if total_reservadas>=1:
                    print(f"\nTotal canchas reservadas: {total_reservadas}")
                    for i in control_reservas.total_reservas:
                        if  fecha_cancha.date() == i[1].date():
                            print(f"Fecha= {fecha_cancha.date()}\tCancha ={i[3]} \tValor_cancha = {i[5]}\tCliente ={i[0]}")
                    input("Presione enter -->")
                    break
                else:
                    print("\nNo hay canchas reservadas ese día")
                    break
            except:
                system("cls")
                print(RED,"\nINGRESASTE MAL LA FECHA, INGRESALA ASÍ AÑO-MES-DÍA ",WHITE)

def dinero_caja():

    #validar reservas
    if len(control_reservas.total_reservas)==0:
        excepciones_time.tiempo("Revisando caja ...","Resultados de la caja")
        print("NO HAY DINERO EN CAJA ")
        input("Presione enter --> ")
    else:
        total=0
        for i in control_reservas.total_reservas:
            #el dinero de la reserva es i[5]

            total+=i[5]
        excepciones_time.tiempo("Ingresando la caja ...","Resultados de la caja");system("cls")
        print(f"\nTOTAL DINERO DE CAJA:  {total}")
        input("Presione enter")



