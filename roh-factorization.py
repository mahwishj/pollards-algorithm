import math
# idx 0 -> i, idx 1 -> i-1

N = 2201 
x_i = [0, 0]
y_i = [0, 0]

# gcd 
g_i = [0, 0]

i = 0

while True:
    #compute next x
    x = (((x_i[0])**2)+2) % N

    # compute next y
    y_sub = (((y_i[0])**2) +2) % N
    y = (((y_sub)**2) +2) % N
    
    x_i[1] = x_i[0]
    x_i[0] = x

    y_i[1] = y_i[0]
    y_i[0] = y

    # compute gcd
    g = math.gcd(abs(x-y), N)
    g_i[1] = g_i[0]
    g_i[0] = g


    #print(g)

    # print(x_i)
    # print(y_i)
    # print(g_i)


    if(g > 1 and g!=N):
        print(i, g)
        print(i/math.sqrt(N))
        break
    i+=1
