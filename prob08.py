# made by Carter
def mass_input():
    i = [input()]
    while i[-1] != '0 0':
        i.append(input())
    return i[:-1]

for case in mass_input():
    a, b = (int(x) for x in case.split())
    r = ('{:b}'.format(n) for n in range(a, b+1))
    even = 0
    for b in r:
        if b.count('1') % 2 == 0:
            even += 1
    print(even)
