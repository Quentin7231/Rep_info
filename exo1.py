def imc():
    taille=float(input("votre taille en mètre : "))
    poids=float(input("votre poids en kilogramme : "))
    imc=poids/(taille*taille)
    return imc
print(imc())