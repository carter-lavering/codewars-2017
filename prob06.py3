# made by Carter
for __ in range(int(input())):
    nums = [int(x) for x in input().split()][1:]
    deltas = [nums[i+1]-nums[i] for i in range(len(nums)-1)]
    out = [nums[0]]
    for d in deltas:
        out.append(out[-1]-d)
    print(' '.join([str(x) for x in out]))
