
def factorial (num):
  fact=1
 
  for i in range(1,num+1):
        fact=fact*i
  return fact

def multiplo3 (num):
  if num%3 == 0 :
    return True


cont3=0
num= int (input("ingrese un numero: "))
factorial(num)
multiplo3(num)

if multiplo3(num):
    cont3 = cont3 +1

    