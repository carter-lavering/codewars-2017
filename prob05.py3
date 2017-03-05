mylist = []
numinputs = int(input())
while numinputs > 0:
    numinputs -= 1
    myinput = input()
    x,y,z = myinput.split()
    mynum = (float(y)/float(z))
    data = x + " " + str(mynum)
    mylist.append(data)

mylist = sorted(mylist, key=lambda x: x.split()[1])
print(mylist[0])
