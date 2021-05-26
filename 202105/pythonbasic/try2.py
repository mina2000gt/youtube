i = open('try2.dat','r').read()
a = 0
b = 0
c = 0
for p in i:
    if i == 'A':
        a += 1
    elif i == 'B':
        b += 1
    else:
        c += 1
print('A:',a,',B:',b,',C:',c)
