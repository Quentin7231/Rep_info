def ajouterCoeff(pol):
    coeff=int(input("choisis ton coeff : "))
    pol.insert(0,coeff)
    return pol

#print(ajouterCoeff([10,5,3]))

def nvpol(n):
    pol=[]
    for i in range(n+1):
        pol=pol+[int(input("valeur : "))]
    return pol


#print(nvpol(int(input("ordre du polynome  : "))))
polyn=nvpol(int(input("ordre du polynome  : ")))

def affichePol(pol):
    poly=""
    o=len(pol)-1
    for i in range(len(pol)-1):
        poly=poly+str(pol[i])+"x^"+str(o)+"+"
        o-=1
    poly=poly+str(pol[len(pol)-1])
    return poly

#print(affichePol(polyn))

def destructeurduniversetdegalaxie(p):
    p=[]
    return p

#print(destructeurduniversetdegalaxie(polyn))

polyn1=nvpol(int(input("ordre du polynome  : ")))

def add(p1, p2):
    p1_rev = p1[::-1]
    p2_rev = p2[::-1]
   
    res = []
    taille_max = max(len(p1), len(p2))
   
    for i in range(taille_max):
        coeff1 = p1_rev[i] if i < len(p1) else 0
        coeff2 = p2_rev[i] if i < len(p2) else 0
        res.append(coeff1 + coeff2)
    res.reverse()
    return res

print(add(polyn, polyn1))