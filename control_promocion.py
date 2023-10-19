from os import system;system("cls")
import time
import excepciones_time
import datetime
#para que de color a las letras 
RED = '\033[31m'
WHITE = '\033[37m'

promociones=[]

def menu_promociones():
    while True:
        system("cls")
        print("=" * 56)
        print("|   CONTROL DE PROMOCIONES DE CANCHAS DEPORTIVAS SAS   |")
        print("=" * 56)
        print("|    1.  --   CREAR DESCUENTO %                        |")
        print("|    2.  --   SALIR                                    |")
        print("=" * 56);print("")
        try:
            opcion = int(input("Ingrese la opcion a ejecutar --> "))   
        except:
            excepciones_time.excepciones()
            continue    

        if opcion==1:
            crear_promocion()
        elif opcion==2:
            break
        else:
            excepciones_time.errores()
             
def crear_promocion():
    #creando promocion
        promo=[]
        while True:
            try:
                #Solicitar la fecha 
                fecha=input("Ingrese la fecha del descuento (día-mes-año) --> ")
                fechapromo=datetime.datetime.strptime(fecha,"%d-%m-%Y")
                try:
                    #solicitar el descuento
                    num_descuento=int(input("Ingrese el numero de descuento %  --> "))
                    promo.append(fechapromo.date())
                    promo.append(num_descuento)
                    promociones.append(promo)
                    excepciones_time.tiempo("Creando promoción ...","Promoción creada")
                    break
                except:
                    excepciones_time.excepciones()
                break
            except:
                print(RED,"Debes ingresar la fecha de descuento así --> día-mes-año ",WHITE)
