'''
5.	Diseñar una rutina que imprima el cartel:
	PRESIONE ENTER 
	PARA CONTINUAR
'''

def cartel():
    print('''
    PRESIONE ENTER
    PARA CONTINUAR
    ''')


desea=int(input("desea imprimir el cartel (1 Si) (2 No) "))
if desea ==1:
    cartel()
else:
    print("Fin del programa")
    