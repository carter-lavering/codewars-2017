L = [1,2,3,4,5,6]
F = [0,1,1,2,3,5]
T = [0,0,1,1,2,4]
N=[1,2,2,3,3,4]
Z=[1,1,1,2,2,3]
P=[0,1,2,3,5,7]
G=[1,2,3,3,4,5]

while True:
    vals = input().split()
    s1 = vals[0]
    s2 = vals[1]
    s3 = vals[2]
    perms = []
    totalPerms = 6*6*6
    isX = False
    if (s3 == 'X'):
        isX = True
        totalPerms = 6*6
    t1 = int(vals[3])
    t2 = int(vals[4])
    t3 = int(vals[5])
    if s1 == 'L':
        s1 = L
    elif s1=='F':
        s1=F
    elif s1=='T':
        s1=T
    elif s1=='N':
        s1=N
    elif s1=='Z':
        s1=Z
    elif s1=='P':
        s1=P
    elif s1=='G':
        s1=G
    if s2 == 'L':
        s2 = L
    elif s2=='F':
        s2=F
    elif s2=='T':
        s2=T
    elif s2=='N':
        s2=N
    elif s2=='Z':
        s2=Z
    elif s2=='P':
        s2=P
    elif s2=='G':
        s2=G
    if s3 == 'L':
        s3 = L
    elif s3=='F':
        s3=F
    elif s3=='T':
        s3=T
    elif s3=='N':
        s3=N
    elif s3=='Z':
        s3=Z
    elif s3=='P':
        s3=P
    elif s3=='G':
        s3=G
    for x in s1:
        for y in s2:
            if not isX:
                for z in s3:
                    perms.append(x+y+z)
            else:
                perms.append(x+y)
    Ts = [t1,t2,t3]
    totals = [0,0,0]
    percents = [0.0,0.0,0.0]
    for index in range(len(Ts)):
        for a in perms:
            if a ==Ts[index]:
                totals[index] += 1
        percents[index] = float(totals[index])/float(totalPerms)
    if not isX:
        print(''.join(s1) + " " + ''.join(s2) + " " + ''.join(s3))
    else:
        print(''.join(s1) + " " + ''.join(s2))
    for index in range(len(Ts)):
        print(''.join(Ts[index]) + ' '.join(totals[index]) + ' '.join(percents[index]) + '%')
        #we're done!