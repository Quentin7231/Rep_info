from random import randint
let=['A','B','C','D','E','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
chi=[0,1,2,3,4,5,6,7,8,9]
n=int(input("nombre plaque a générer : "))
plaque=""
for i in range(n):
    plaque=plaque+let[randint(0,22)]+let[randint(0,22)]+"-"+str(chi[randint(0,9)])+str(chi[randint(0,9)])+str(chi[randint(0,9)])+"-"+let[randint(0,22)]+let[randint(0,22)]
    if plaque[1]=='S' and plaque[0]=='S' or plaque[7]=='S' and plaque[8]=='S':
        plaque=''
    print(plaque)
    plaque=''

