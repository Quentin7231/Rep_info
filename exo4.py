i=1
pi=3
n=4*int(input("nombre d'approximation : "))
while n<0:
    print("nombre négatif impossible")
    n=4*int(input("nombre d'approximation : "))
while i<n:
    pi=pi+4/((i+1)*(i+2)*(i+3))-4/((i+3)*(i+4)*(i+5))
    i+=4
    print(pi)