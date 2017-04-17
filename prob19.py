from itertools import permutations, combinations

# Basically magic
s, v = zip(*[sorted([int(x) for x in input().split()]) for __ in range(int(input().split()[0]))])

def compute_k(s, v):
    for p in combinations(range(len(s)), 2):
        print(s[p[0]], v[p[0]], 'largest')
        print(s[p[1]], v[p[1]], 'smallest')

compute_k(s, v)
