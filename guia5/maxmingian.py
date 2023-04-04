def funcion():
        media = (tmaxima+tminima)/2
        print ("Su media es: ",media)
        
contador = 0
dias = int(input("Ingrese la cantidad de dias que se van a introducir: "))
while contador != dias:
        tmaxima = int(input("Ingrese la temperatura maxima: "))
        tminima = int(input("Ingrese la temperatura minima: "))
        funcion()
        contador = contador+1