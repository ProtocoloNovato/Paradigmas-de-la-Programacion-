
def suma_dias(fecha,cantdias):
    dia = int(str(fecha)[6:8])
    mes = int(str(fecha)[4:6])
    anio = int(str(fecha)[0:4])
    if dia > 0 and dia < 32 and mes > 0 and mes < 13:
        nuevo_dia = dia + cantdias
        nuevo_mes = mes
        nuevo_anio = anio
        if nuevo_dia > 31:
            while nuevo_dia > 31: 
                nuevo_dia = nuevo_dia - 31
                nuevo_mes += 1
            if nuevo_mes > 12:
                while nuevo_mes > 12:
                    nuevo_mes = nuevo_mes - 12
                    nuevo_anio += 1

    fecha_nueva=(f"{nuevo_dia}/{nuevo_mes}/{nuevo_anio}")
    return fecha_nueva

fecha = input("Ingrese una fecha en formato AAAAMMDD: ")
while len(fecha) != 8:
    print("Error - Ingrese 8 digitos")
    fecha = input("Ingrese una fecha en formato AAAAMMDD: ")

cantdias = int(input("Ingrese una cantidad de días: "))
print(f"\nLa nueva fecha es: {suma_dias(fecha, cantdias)}")







