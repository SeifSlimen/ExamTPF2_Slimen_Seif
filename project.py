def somme(T):
    s = 0
    for t in T:
        s += t
    return s

Data = [1,3,5]
som = sum(Data)

if Data:
    print('la somme est :',sum(Data))
    print('le min est :',min(Data))
    print('le max est :',max(Data))
else:
    print('la liste est vide')
