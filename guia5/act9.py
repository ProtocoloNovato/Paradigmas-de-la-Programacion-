'''
Desarrollar un procedimiento tal que dada una hora (HHMMSS) y 
un tiempo también en formato HHMMSS devuelva la nueva hora que surge 
de sumar el tiempo a la hora  inicial, considere también si cambió el día.
'''

def fecha(string):
    fecha = '{}/{}/{}'.format(string[6:8], string[4:6], string[2:4])
    return fecha

string = input("Ingrese fecha en formato AAAAMMDD: ")
while len(string)!=8:
    print("Error - Ingrese 8 digitos")
    string = input("Ingrese fecha en formato AAAAMMDD: ")

fecha(string)
print(f"\nLa fecha es {fecha(string)}")