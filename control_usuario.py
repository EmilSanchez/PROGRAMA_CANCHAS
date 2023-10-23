from os import system;system("cls")
import excepciones_time

RED = '\033[31m'; WHITE = '\033[37m'
#user_responsables=[[Nombre,cedula,contraseña]]
users_responsables=[["Luisa Araque","1065871433","luisa22"]]

def iniciocont_usuario():
    #Menu de control de usuarios
    while True: 
        system("cls");print("=" * 49)
        print("|  CONTROL DE USUARIO DE CANCHAS DEPORTIVAS SAS |")
        print("=" * 49)
        print("|    1.  --   REGISTRAR RESPONSABLE             |")
        print("|    2.  --   ELIMINAR RESPONSABLE              |")
        print("|    3.  --   ACTUALIZAR RESPONSABLE            |")
        print("|    4.  --   CONSULTAR RESPONSABLE             |")
        print("|    5.  --   SALIR                             |")
        print("=" * 49); print("")
            
        try:
            opcion = int(input("Ingrese la opcion a ejecutar --> "))         
        except:
            excepciones_time.errores()
            continue    

        if opcion==1:
            agregarrespon()
        elif opcion==2:
            eliminarrespon()
        elif opcion==3:
            actualizarrespon()
        elif opcion==4:
            existencia, mensaje=buscar_respon()
            if existencia:
                print(f"Se ha finalizado la consulta del responsable")
            else:
                print(mensaje)
            input("Presione enter --> ")
        elif opcion==5:
            break
        else:
            excepciones_time.errores()


def agregarrespon():
    system("cls");nuevo_repon=[]
    print("\n            REGISTRAR RESPONSABLE           ")

    #pedir datos
    nombre=input("\nIngrese el nombre y apellido del responsable a agregar --> ").title()
    cc=input("Ingrese la cédula del responsable --> ")
    contraseña_respon=input(f"Ingrese la contraseña  para el registro de cuenta del responsable -->")
    
    #Agregar dato 
    nuevo_repon.append(nombre)
    nuevo_repon.append(cc)
    nuevo_repon.append(contraseña_respon)
    
    #Registrar responsable
    users_responsables.append(nuevo_repon)
    excepciones_time.tiempo("Registrando responsable...","Responsable registrado")

def buscar_respon():

    #Validar existencia de responsable
    if len(users_responsables)==0:
        return False,"No HAY RESPONSABLES REGISTRADO"
    else:
        #pedir dato
        cc=input("\nIngrese la identificación  del responsable --> ")
        excepciones_time.tiempo("Buscando responsable ...","RESULTADOS:")
        system("cls"); contador=0


        for i in users_responsables:
            #Verificar cedula 
            if i[1] == cc :
                print(f"\nResponsable: {i[0]} \t\t\t Identificación: {cc} \t\t\tContraseña: {i[2]}")
                return True,i
        if contador == 0 :
            return False,"NO HAY RESPONSABLES REGISTRADOS CON ESTA IDENTIFICACIÓN"
        
def eliminarrespon():
    #Validar existencia de responsables
    existencia_respon,responsable_mensaje=buscar_respon()
    if existencia_respon:
        users_responsables.remove(responsable_mensaje)
        excepciones_time.tiempo("Eliminando responsable ...","Responsable eliminado ")
    else:
        print(responsable_mensaje)
        input("Presione enter")


def actualizarrespon():

    #Buscar responsable a actualizar
    existencia_respon,responsable_mensaje=buscar_respon()
    if existencia_respon:
        users_responsables.remove(responsable_mensaje)
        while True:
            print("\n       NUEVO DATO DEL RESPONSABLE           ")
            print("\n1.  --    ACTUALIZAR NOMBRE         ")
            print("2.  --    ACTUALIZAR CEDULA         ")
            print("3.  --    ACTUALIZAR CONTRASEÑA         ")
            print("4.  --    FINALIZAR ACTUALIZACIÓN   ")        
            try:
                opc=int(input("\nIngrese la opción del dato a actualizar --> "))
                if opc>=1 and opc<=3:
                    nuevo_dato=input("Ingrese el nuevo dato del responsable --> ")
                    #Cambiar el dato 
                    responsable_mensaje[opc-1]=nuevo_dato
                    excepciones_time.tiempo("Actualizando dato ...","Dato actualizado");system("cls")

                elif opc==4:
                    #Ingresa la actualizacion del responsable
                    users_responsables.append(responsable_mensaje)
                    excepciones_time.tiempo("Actualizando responsable ...","Responsable actualizado")
                    break
                else:
                    excepciones_time.errores()
            except:
                excepciones_time.excepciones()

    else:
        print(responsable_mensaje);input("Presione enter --> ")



