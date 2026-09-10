age=int(input("votre age : "))
while age<0:
    print("age négatif impossible")
    age=int(input("votre age : "))
if age>=2:
    agec=(10.5)*2+4*(age-2)
else:
    agec=10.5
print(agec)