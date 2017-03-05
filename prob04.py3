def magic():
    datainput = input()
    x,y = datainput.split()
    miles = float(y)/60
    print(float(x)/miles)

numtimes = int(input())
while numtimes > 0:
    magic()
    numtimes -= 1