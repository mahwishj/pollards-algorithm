import math
N = 10000000000000000000009434343434343434465890000000000000000114155555555555555573169

a = 2
for j in range (2, 10**7):
    a = pow(a, j, N)
    d = math.gcd(a-1, N)
    if 1<d and d<N:
        print(d)
        break
    
