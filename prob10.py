# made by Carter
import string

ascii = string.ascii_letters + '1234567890'
for __ in range(int(input())):
    s = input()
    
    L = ''.join([c for c in s if c in ascii]).lower()
    i2 = 0
    m = dict()  # M for map
    for i, c in enumerate(s):
        if c in ascii:
            m[i2] = i
            i2 += 1
    slices = []
    for begin in range(len(L)):
        for end in range(begin+2, len(L)+1):
            slice = L[begin:end]
            if slice == slice[::-1]:
                slices.append((begin, end))
    slices = sorted(slices, key=lambda x: x[1]-x[0], reverse=True)
    if not slices:
        print('NO PALINDROME')
        continue
    ls = slices[0]
    print(s[m[ls[0]]:m[ls[1]-1]+1])
