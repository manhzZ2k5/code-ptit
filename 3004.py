t=int(input())
for i in range(t):
    test=[]
    n=int(input())
    test=input().split()
    test.sort()
    a=''
    b=''
    for j in range(n):
        if(int(j)%2==0):
            a+=test[j]
        else:
            b+=test[j]
    print(int(a)+int(b))