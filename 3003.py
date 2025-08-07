def tinhtong(a,b):
    Max=0
    for i in range(a):
        Max+=(i*b[i])
    return Max
t=int(input())
MOD = 10**9 + 7
for i in range(t):
    n=int(input())
    number=[]
    number=list(map(int,input().split()))
    number.sort()
    print(tinhtong(n,number)%MOD)
