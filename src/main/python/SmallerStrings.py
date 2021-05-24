MOD = 10**9+7
t = int(input())
for i in range(1, t + 1):
    N, K =map(int,input().split())
    S = input()

    h = (N+1)//2
    s1 = S[:h]
    if N%2 == 0:
        s3 = s1+s1[::-1]
    else:
        s3 = s1 + s1[:(h-1)][::-1]
    
    value = 0
    p = h-1
    for c in s1:
        value += (ord(c) - ord('a')) * pow(K,p,MOD)
        p -=1 

    if S>s3:
        value +=1

    print("Case #{}: {}".format(i, value%MOD))
