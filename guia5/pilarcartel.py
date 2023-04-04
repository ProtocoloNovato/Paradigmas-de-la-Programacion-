import time
def texto (text, n, intervalo=2): #2 = seg
  for _ in range (n):
    print (text)
    time.sleep (intervalo)
texto ("""PRESIONE ENTER 
PARA CONTINUAR
""", 3) #3 = veces