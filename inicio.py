from os import system
system("cls")
import administrador
import responsable
import excepciones_time
                    
def programa():
    #validar usuario
    while(True):

        print("=" * 44)
        print("|          CANCHAS DEPORTIVAS SAS          |")
        print("=" * 44)
        print("|    1.  --   ADMINISTRADOR                |")
        print("|    2.  --   RESPONSABLE                  |")
        print("|    3.  --   SALIR                        |")
        print("=" * 44); print("")

        try:
            opcion = int(input("Ingrese la opcion a ejecutar --> "))         
        except:
            #Mensaje de ERROR
            excepciones_time.excepciones()
            continue    

        if opcion==1:
            excepciones_time.tiempo("Ingresando ...","Ingreso exitoso")
            administrador.validar_admin()
        elif opcion==2:
            excepciones_time.tiempo("Ingresando ...","Ingreso exitoso")
            responsable.validar_respon()
        elif opcion==3:
            break
        else:
            excepciones_time.errores()

if __name__=="__main__":
    programa()