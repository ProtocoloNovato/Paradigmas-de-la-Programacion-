


def suma_hhmmss(hhmmss,hhmmss2):
    

    tiempo=hhmmss+hhmmss2
    #234654
    #23----
    #--46--
    #----54
    horas = int(str(tiempo)[0:2])
    minutos = int(str(tiempo)[2:4])
    segundos = int(str(tiempo)[4:6])
    dia=0

    if segundos > 60:
        while segundos > 60:
            segundos=segundos-60
            minutos+=1
        if minutos > 60:
            while minutos > 60:
                minutos=minutos-60
                horas+=1
            if horas > 24:
                while horas > 24:
                    horas=horas-24
                    dia+=1

    if dia == 1:
        nuevo_horario=(f'\nNuevo horario {dia}dia {horas}hs {minutos}min {segundos}s')
    else:
        nuevo_horario=(f'\nNuevo horario {horas}hs {minutos}min {segundos}s')
    return nuevo_horario



print ("----- 1er Horario -----")

segundo = float(input("Ingrese segundo: "))
while segundo<00 or segundo>60 or segundo%1!=0: 
    print("Error - Ingrese numeros entre el rango de 1 y 60")
    segundo = float(input("Ingrese segundo: "))

minuto = float(input("Ingrese minuto: "))
while minuto<00 or minuto>60 or minuto%1!=0: 
    print("Error - Ingrese numeros entre el rango de 1 y 60")
    minuto = float(input("Ingrese minuto: "))

hora = float(input("Ingrese hora: "))
while hora<00 or hora>24 or hora%1!=0: 
  print("Error - Ingrese numeros entre el rango de 1 y 60")
  hora = float(input("Ingrese hora: "))

hhmmss = (hora * 10000) + (minuto * 100) + (segundo)
print ("Fecha en formato HHMMSS: ", int(hhmmss))

print("\n----- 2do Horario -----")

segundo2 = float(input("Ingrese segundo: "))
while segundo2<00 or segundo2>60 or segundo2%1!=0:
  segundo2 = float(input("ERROR- Ingrese segundo: "))

minuto2 = float(input("Ingrese minuto: "))
while minuto2<00 or minuto2>60 or minuto2%1!=0: 
  minuto2 = float(input("ERROR - Ingrese minuto: "))

hora2 = float(input("Ingrese hora: "))
while hora2<00 or hora2>24 or hora2%1!=0: 
  hora2 = float(input("ERROR - Ingrese hora: "))

hhmmss2 = (hora2 * 10000) + (minuto2 * 100) + (segundo2)
print ("Fecha en formato HHMMSS: ", int(hhmmss2))


print(suma_hhmmss(hhmmss,hhmmss2))