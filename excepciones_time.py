from os import system; system("cls")
import time
#para que de color a las letras
RED = '\033[31m'
WHITE = '\033[37m'


def tiempo(mensaje_proceso,mensaje_finalizado):
    for i in range(2):
        system("cls")
        print(mensaje_proceso)
        time.sleep(0.5)

    system("cls")
    print(mensaje_finalizado)
    input("Presione Enter .. --> ")

def excepciones():
    print(RED,"")
    print("UPS! DEBES INGRESAR UN ENTERO POSITIVO VALIDO :)...")
    print(WHITE,"")
    input("Presione Enter.. --> ")
    system("cls")

def errores():
    print(RED,"")
    print("Esa opción no existe, ingrese una valida")
    print(WHITE,"")
    input("Presione Enter para intentarlo nuevamente --> ")
    system("cls")  

'''
como crear una resera y como editar una reserva 
pero para crear una reserva debo buscar un cliente y debo buscar una cancha
si voy hacer una reserva soy el responsable o el administrador-->vas a reservar?--> si -->  que cancha va a reservar? 
                                                                                       -->  quien la va a reservar? #el cliente "nombre del cliente"
                                                                                       -->  En que horario? en este horario "en este horario"
                                                                                       -->  cuanto vale? #el precio
                                                                                       -->
                                                                                -> No


no se puede hacer una reserva sin haber un cliente, si no hay cliente registrado, antes de crear la reserva si retorna la cantidad de cliente 0, se le dice que no puede hacer una reserva sin registrar un cliente,se le manda a menu principal a que registre el cliente y de ahí traca

si quiere arbitros, y si no hay arbitros regitrados hacer ...

'''