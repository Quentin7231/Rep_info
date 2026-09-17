def binaire():
    résultat=''
    q=int(input('nombre a convertir en base 2 : '))
    while q>0:
        r=q%2
        résultat=str(r)+résultat
        q=q//2
    return résultat

print(binaire())