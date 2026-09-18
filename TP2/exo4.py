def score(vs):
    pile = []
    for i in vs:
        if i=='+':
            if len(pile)>1:
                pile.append(pile[-1]+pile[-2])
            else:
                pile.append(pile[-1])
        elif i=='C':
            pile.pop()
        elif i=='D':
            pile.append(2*pile[-1])
        else:
            pile.append(int(i))

    return sum(pile)

print(score(["10", "C", "D", "+", "5", "+"]))
