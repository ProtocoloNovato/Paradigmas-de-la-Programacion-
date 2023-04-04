'''
6.	Desarrollar un procedimiento que imprima una fecha en formato DD/MM/AA. 
El dato que recibe es un longint con una fecha en formato aaaammdd.
'''
def fecha(string):
    fecha = '{}/{}/{}'.format(string[6:8], string[4:6], string[2:4])
    #20191215
    #12345678
    #2-4 4-6 6-8
    #15 12 19
    return fecha

string = input("Ingrese fecha en formato AAAAMMDD: ")
while len(string)!=8:
    print("Error - Ingrese 8 digitos")
    string = input("Ingrese fecha en formato AAAAMMDD: ")

fecha(string)
print(f"\nLa fecha es {fecha(string)}")


