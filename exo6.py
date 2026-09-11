def calculateur():  
    o=str(input("choisissez votre opérateur (a)ddition, (s)oustraction, (m)ultiplication et(d)ivision : "))
    while o!="a"and o!='A' and o!="s"and o!='S' and o!="m"and o!='M' and o!="d" and o!='D':
        print("calcul non compris!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        if 'n'==(str(input("un autre calcul? : (o) ou (n)"))):
            exit()
        o=str(input("choisissez votre opérateur (a)ddition, (s)oustraction, (m)ultiplication et(d)ivision : "))
    val1=float(input("valeur : "))
    val2=float(input("valeur : "))
    if o=='a'or'A':
        c=val1+val2
    elif o=='s'or'S':
        c=val1-val2
    elif o=='m'or'M':
        c=val1*val2
    elif o=='d'or'D':
        if val2==0:
            val2=float(input("changez la valeur : "))
        c=val1/val2
    return c
print(calculateur())
         