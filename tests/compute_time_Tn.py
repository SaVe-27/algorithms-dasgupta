import time

def T_n(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return 3 + T_n(n-2) + T_n(n-1)

def F_n(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F_n(n-2) + F_n(n-1)

def test(n):
    init = time.time()
    F_n(n)
    final = time.time()
    print(final-init)

z = 100

#test(z)

print(f"  n | T_n | F_n")
for i in range(0,z):
    print(f"{i} | {T_n(i)} | {F_n(i)}")
