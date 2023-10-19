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
