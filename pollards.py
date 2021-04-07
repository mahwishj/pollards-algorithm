import math
N = 19048567

a = 2
for j in range (2, 1000):
    a = pow(a, j, N)
    d = math.gcd(a-1, N)
    if 1<d and d<N:
        print(d)
        break
    
