from random import randint
a=[]
b=False
for i in range(randint(2,100)):
    c=randint(0,500)
    for j in range(len(a)):
        if c==a[j]:
            b=True
    a=a+[c]
            
        
print(a)
if b==True:
    print("pas tous différent")
else:
    print("ils sont tous différents")