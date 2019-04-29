a = 'i love you do you love me?'
b = a.split(' ')

c = dict()

for i in range(len(b)):
    c[b[i]] = 1
    for j in range(len(b)):
        if((i != j) and (b[i] == b[j])):
            c[b[i]] += 1
    

print(c)
