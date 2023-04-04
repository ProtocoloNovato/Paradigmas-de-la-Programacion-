'''
7.	Desarrollar una rutina tal que dados una base y un exponente, 
enteros positivos, calcule  y retorne la potencia.
'''
def potencia_num_positivos(a,b,c):
    a=base
    b=exponente
    c=base2
    if exponente == 0:
        potencia=1
        return potencia
    cont=2
    while b >= cont:
        potencia=a*c
        c=potencia
        cont+=1
    return potencia
    

base=int(input("base: "))
while (base <= 0 ):
    print("Error - Ingrese numeros positivos")
    base=int(input("base: "))
base2=base

exponente=int(input("exponente: "))
while (exponente <= -1):
    print("Error - Ingrese numeros positivos")
    exponente=int(input("exponente: "))

print(f"\nLa potencia es: {potencia_num_positivos(base,exponente,base2)}")


