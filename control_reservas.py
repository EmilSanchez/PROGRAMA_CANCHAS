from os import system; system ("cls")
import control_clientes
import datetime
import control_promocion
import excepciones_time
import control_arbitros
import random
RED = '\033[31m'
WHITE = '\033[37m'

#total reservas=[[cliente , fecha_inicio, fecha_fin, cancha, arbitro, costo]]
total_reservas = []  

def disponibilidad_cliente():
    while True:
        system("cls")
        print("\n    BIENVENIDOS AL SISTEMA DE RESERVAS DE CANCHAS DEPORTIVAS SAS  ")
        print("\nEL COSTO DE LA CANCHA POR HORA ES DE $30000")

        opc=input("\nDesea registrar una reserva? (si/no) --> ").lower()
        if opc=="no":
            break
        elif opc=="si":

            #Verificar registro del cliente
            existencia_cliente,nombre_cliente=control_clientes.consultar_cliente()

            #SI cliente no está registrado
            if existencia_cliente==False:
                print(RED,f"\nNO SE PUEDE RESERVAR UNA CANCHA SI {nombre_cliente}",WHITE)
                input("\nPresione enter para registrar el cliente --> ")

                #registrar cliente
                nombre_cliente=control_clientes.registrar_cliente()

            #Reservar fecha
            fechas_reserva(nombre_cliente)
        else: 
            continue

def fechas_reserva(nombre_cliente):
    system("cls")
    print("\n    SISTEMA DE RESERVAS DE CANCHAS DEPORTIVAS SAS  ")

    while True:
        try:

            #Solicitar la fecha
            fecha_str= input("\nIngrese la fecha de reserva  (día-mes-año) --> ")

            #%dia-%mes-%año
            fecha=datetime.datetime.strptime(fecha_str,"%d-%m-%Y")
            hora(fecha,nombre_cliente)
            break
        except:
            system("cls")
            print(RED,"\nINGRESASTE MAL LA FECHA, INGRESALA ASÍ DÍA-MES-AÑO ",WHITE)
            continue

def hora(fecha,nombre_cliente):
    while True:
        datos_reserva=[]
    
        #horarios
        print("\nHORARIO DE LA MAÑANA de 8:00 a 12:00 ")
        print("HORARIO DE LA TARDE de 15:00 a 19:00 ")

        try:
            #Solicitar las horas
            hora_inicio_str=input("\nIngrese la hora de inicio (hora:minutos) --> ")
            hora_inicio=datetime.datetime.strptime(hora_inicio_str,"%H:%M")
            hora_fin_str=input("Ingrese la hora de fin (hora:minutos) --> ")
            hora_fin=datetime.datetime.strptime(hora_fin_str,"%H:%M")

            #Verificar las horas ingresadas
            if hora_inicio<hora_fin:

                #Establecer la fecha de incio y fin
                fecha_inicio=datetime.datetime.combine(fecha.date(),hora_inicio.time())
                fecha_fin=datetime.datetime.combine(fecha.date(),hora_fin.time())

                #Verificar los horarios
                if  hora_inicio>=datetime.datetime.strptime("8:00","%H:%M") and hora_fin<=datetime.datetime.strptime("12:00","%H:%M") or hora_inicio>=datetime.datetime.strptime("15:00","%H:%M") and hora_fin<=datetime.datetime.strptime("19:00","%H:%M"):
                    break
                else:
                    system("cls")
                    print(RED,"\nLAS HORAS INGRESADAS NO ESTÁN DENTRO DE LOS HORARIOS")
                    input("Presione enter -->")
            else:
                system("cls")
                print(RED,"\nINGRESASTE MAL EL HORARIO, LA HORA DE INCIO NO PUEDE SER MAYOR A LA HORA DE FIN",WHITE)
                input("Presione enter -->")
        except:
            system("cls")
            print(RED,"\nIngresaste mal las horas  por favor ingresala así:  horas:minutos  ",WHITE)
            input("Presione enter")

    #Disponibilidad cancha 
    res,cancha=dispon_canchas(fecha_inicio,fecha_fin)
    if res==True:

        #calcular costo
        costo_reserva,descuento=calcular_costo(fecha_inicio,fecha_fin)

        #validar árbitro
        while True:
            opc=input("La reserva tendrá árbitro? (si/no) --> ").lower()
            if opc=="si":
                arbitro_seleccionado=dispon_arbitro(fecha_inicio,fecha_fin);break
            elif opc=="no":
                arbitro_seleccionado="Ninguno";break
            else:
                print(RED,"Ingrese si o no",WHITE,"\n")
                continue

        #Realizar reserva
        datos_reserva.append(nombre_cliente);datos_reserva.append(fecha_inicio);datos_reserva.append(fecha_fin);datos_reserva.append(cancha);datos_reserva.append(arbitro_seleccionado);datos_reserva.append(costo_reserva)       
        total_reservas.append(datos_reserva)
        excepciones_time.tiempo("Realizando reserva ...","Reserva realizada");system("cls")
        print(f"\nReserva realizada a nombre de {nombre_cliente} el día  {fecha.date()}  de  {hora_inicio_str} a {hora_fin_str}") 
        print(f"El Costo de la reserva es : ${costo_reserva:.2f} \t Descuento: {descuento} %    \t Árbitro: {arbitro_seleccionado}")
        input("\nPresione enter -->")
                                
    else:
        print("No hay canchas disponibles en este horario")
        input("presione enter --> ")   
        fechas_reserva(nombre_cliente)                


def dispon_canchas(fecha_inicio,fecha_fin):

    print("\n           CANCHAS         \n")
    while True:
        #mostrar canchas
        for i in range (1,6):
            print(f"Cancha {i}")
        try:
            cancha=int(input("\nIngrese la opción de cancha -->"))
            if cancha>=1 and cancha<=5:

                # Verifica si la cancha está disponible 
                if len(total_reservas)==0:
                    return True,cancha
                else:
                    for i in total_reservas:
                        #i[2]=fecha fin , i[1]=fecha inicio  e i[3]=cancha reservadas
                        if fecha_inicio<i[2] and fecha_fin>i[1]  and cancha==i[3] :
                            return False,cancha
                    return True,cancha
            else:
                excepciones_time.errores()
        except:
            excepciones_time.excepciones()



def dispon_arbitro(fecha_inicio,fecha_fin):
    contador=1
    while contador<=len(control_arbitros.arbitros):
        disponible=True

        #selecciona el arbitro
        arbitro_seleccionado=random.choice(control_arbitros.arbitros)

        #Verificar la disponibilidad del árbitro
        for i in total_reservas:
            # i[4]=arbitro reservado   
            if (fecha_inicio<i[2] and fecha_fin>i[1])  and arbitro_seleccionado==i[4] :
                disponible=False
        
        #Arbitro disponible
        if disponible!=False:
            return arbitro_seleccionado
        contador+=1
    print("No hay árbitros disponibles");input("Presione enter --> ")
    arbitro_seleccionado="No hay árbitro disponible"
    return arbitro_seleccionado


def calcular_costo(fecha_inicio, fecha_fin):

    costo_por_hora = 30000 #costo de la cancha por hora
    tiempo_reservado = fecha_fin - fecha_inicio  

    # Calcula el costo en función de las horas
    costo_reserva = costo_por_hora * tiempo_reservado.total_seconds() /3600

    #Verificar si hay promociones
    for i in control_promocion.promociones:

        #i[0]=fecha de descuento, i[1]=numero de descuento
        if fecha_inicio.date()==i[0]:
            descuento=i[1]/100
            total=costo_reserva-(costo_reserva*descuento)
            return total,i[1]
    return costo_reserva,0