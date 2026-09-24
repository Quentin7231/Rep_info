def recurs(n):
    while n!=1:
        r=n%2
        if r==0:
            n=n/2
        else:
            n=n*3+1
        print(n)
    return n

print(recurs(7))