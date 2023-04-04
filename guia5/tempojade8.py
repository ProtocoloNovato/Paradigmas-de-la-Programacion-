def fecha():
    string = input("Ingrese fecha en formato AAAAMMDD: ")
    sdia=string[6:8] # Separe por dia y mes y anio
    smes=string[4:6]
    sanio=string[0:4]
    cant =int(input("Ingrese cantidad de dias "))
    dia=int(sdia)
    mes=int(smes)
    anio=int(sanio)
    #verificar el mes (para saber si son 29 , 28 , 30 o 31)
    if cant<30:
        dia= dia + cant

    return dia, mes,anio


#Programa principal
dia,mes,anio=fecha() 
print (str(dia) + "/" +str(mes) + "/" +str(anio))