# made by Luke
import math
for T in range(int(input())):
    X0, A, B, C, M, N, errorVal = [float(v) for v in input().split()]
    ansOld = 1
    ans = X0
    cError = 10000
    counter = 1
    p = True
    while cError > errorVal:
        ansOld = ans
        ans = C + (A*ans+M)/(B*ans+N)
        cError = math.fabs(ansOld - ans) #calculate new error
        #print("new error: " + str(cError)) # TODO comment
        counter = counter + 1
        if (counter > 100): #diverge
            print('DIVERGES')
            p = False
            break
    if p:
        print(ans)
