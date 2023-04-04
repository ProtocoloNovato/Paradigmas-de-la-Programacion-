a=int(input("numero: "))
b=int(input("numero: "))

while a > 1 and b >=2:
    if a % 2 == 0:
        reduzcoa=a//2
        a=reduzcoa
    if b % 2 == 0:
        reduzcob=b//2
        b=reduzcob

print(reduzcoa)
print(reduzcob)