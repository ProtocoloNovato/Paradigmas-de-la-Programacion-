'''
Desarrollar una rutina tal que dada una fecha (AAAAMMDD) y un número natural 
que representa una cantidad de días, calcule y retorne la nueva fecha en 
tres parámetros  año (AAAA), mes (MM) y día (DD) que resulte de incrementar
al parámetro fecha con el parámetro cantidad de días. 
'''
def fecha(string):
    fecha = '''
    {}
    {}
    {}
    '''.format(string[6:8], string[4:6], string[2:4])
    return fecha


string = input("Ingrese fecha en formato AAAAMMDD: ")
while len(string)!=8:
    print("Error - Ingrese 8 digitos")
    string = input("Ingrese fecha en formato AAAAMMDD: ")
cant_dias=int(input("ingrese la cantidad de dias: "))

fecha(string)
print(f"\nLa fecha es {fecha(string)}")


