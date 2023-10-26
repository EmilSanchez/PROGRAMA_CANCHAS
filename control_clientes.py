from os import system;system("cls")
import excepciones_time

#clientes=[nombre,cedula,teléfono]
clientes=[]

def menu_clientes():
    while True:
        #Menu de clientes
        system("cls")
        print("=" * 56)
        print("|    CONTROL DE CLIENTES DE CANCHAS DEPORTIVAS SAS     |")
        print("=" * 56)
        print("|    1.  --   CONSULTAR CLIENTE                        |")
        print("|    2.  --   REGISTRAR CLIENTE                        |")
        print("|    3.  --   ACTUALIZAR CLIENTE                       |")
        print("|    4.  --   ELIMINAR  CLIENTE                        |")
        print("|    5.  --   SALIR                                    |")
        print("=" * 56);print("")

        try:
            opcion = int(input("Ingrese la opcion a ejecutar --> "))   
        except:
            excepciones_time.excepciones()
            continue    

        if opcion==1:
            #buscar cliente
            existencia_clientes,mensaje_cliente=consultar_cliente()
            if existencia_clientes==True:
                print(f"\nSe ha finalizado la consulta del cliente")
            else:
                print(mensaje_cliente)
            input("Presione enter --> ")

        elif opcion==2:
            nombre_cliente=registrar_cliente()
            print(f"Se ha finalizado el registro del cliente {nombre_cliente}")

        elif opcion == 3:
            actualizar_cliente()
        elif opcion==4:
            eliminar_cliente()
        elif opcion==5:
            break
        else:
            excepciones_time.errores()
            

def consultar_cliente():
    #validar existencia de clientes
    if len(clientes)==0:
        return False,"NO HAY CLIENTES REGISTRADOS"
    else:
        #Buscar al cliente
        consulta = input("Ingrese la cédula del cliente  --> ")
        excepciones_time.tiempo("Consultando cliente ...","RESULTADOS:");system("cls")
        contador=0
        for i in clientes:
            if consulta == i[1] :
                print(f"\nCliente: {i[0]} \tIdentificación: {consulta}\tTelefono: {i[2]}")
                contador+=1
                return True,i
        if contador == 0:
            return False,"NO HAY CLIENTES REGISTRADOS CON ESTA CÉDULA"
        

def registrar_cliente():
    datos_cliente=[];system("cls")
    print("\n          REGISTRAR CLIENTE           ")
    #pedir datos
    nombre=input("\nIngrese el nombre y apellido del cliente --> ").title()
    cc=input("Ingrese la cédula del cliente --> ")
    tel=input("Ingrese el teléfono del cliente --> ")

    #Guardar datos
    datos_cliente.append(nombre);datos_cliente.append(cc);datos_cliente.append(tel)
    clientes.append(datos_cliente)
    excepciones_time.tiempo("Registrando cliente ...","Cliente  registrado")
    return nombre

def actualizar_cliente():
    existencia, mensaje_cliente=consultar_cliente()
    if existencia:
        clientes.remove(mensaje_cliente)
        while True:
            print("\n       NUEVO DATO DEL CLIENTE           ")
            print("\n1.  --    ACTUALIZAR NOMBRE         ")
            print("2.  --    ACTUALIZAR CEDULA         ")
            print("3.  --    ACTUALIZAR TELÉFONO         ")
            print("4.  --    FINALIZAR ACTUALIZACIÓN   ")        
            try:
                opc=int(input("\nIngrese la opción del dato a actualizar --> "))
                if opc>=1 and opc<=3:
                    nuevo_dato=input("Ingrese el nuevo dato del cliete --> ")
                    mensaje_cliente[opc-1]=nuevo_dato
                    excepciones_time.tiempo("Actualizando dato ...","Dato actualizado");system("cls")

                elif opc==4:
                    clientes.append(mensaje_cliente)
                    excepciones_time.tiempo("Actualizando cliente ...","Cliente actualizado")
                    break
                else:
                    excepciones_time.errores()
            except:
                excepciones_time.excepciones()
    else:
        print(mensaje_cliente)
        input("Presione enter --> ")



def eliminar_cliente():
    existencia, mensaje_cliente=consultar_cliente()
    if existencia:
        clientes.remove(mensaje_cliente)
        excepciones_time.tiempo("Eliminando cliente ...","Cliente eliminado ")
    else:
        print(f"{mensaje_cliente}")
        input("Presione enter")

