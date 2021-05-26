s = '01010010'
zero = 0
one = 0
for c in s:
    if c == '0':
        zero += 1
    else:
        one += 1
print('0: ',zero, ',1: ',one)
