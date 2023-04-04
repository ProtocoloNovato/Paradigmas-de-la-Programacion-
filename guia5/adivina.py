import random
print ("Adivine un numero entre 1 y 5")
while  True:
    num=int(input("Introduce un numero: "))
    magia=random.randint(1,5)
    if num==magia:
        print("ganaste!")
    else:
        print("perdiste")
        print(f"el numero es: {magia}")
    turno=int(input("desea seguir jugando? (1 si) (2 no)"))
    if turno !=1:
        break
print ("hasta luego")
