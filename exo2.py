a=[]
n=1
while n>0:
    n=float(input("votre nombre : "))
    if n>0:
        a=a+[n]
max=a[0]
min=a[0]
moy=0
for i in range(len(a)):
    if max<a[i]:
        max=a[i]   
    if min>a[i]:
        min=a[i]
    moy=moy+a[i]
moy=moy/len(a)
print(max, min, moy)