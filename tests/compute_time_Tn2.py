import time

def F_n2(n):
    if n == 0: return 0
    f = [0 for _ in range(0,n+1)]
    
    f[0] = 0
    f[1] = 1
    
    if n > 1:
        for i in range(2, n+1):
            f[i] = f[i-1] + f[i-2]
            
    return f[n]

def test(n):
    init = time.time
    init = time.time()
    F_n2(n)
    final = time.time()
    print(final-init)

z = 200000

test(z)