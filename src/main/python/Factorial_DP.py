t = int(input())

fac = []
fac.append(1)
for i in range(t):
    N = int(input())
    
    if len(fac) < N + 1:
        for f in range(len(fac),N+1):
            fac.append((f * fac[-1])%1000000007)

    print(fac[N])
