#You are given two integers N and K. Consider all ways to represent N as the sum of exactly K distinct positive integers x1,x2,…,xK — in other words, xi>0 for each valid i, xi≠xj for each valid i≠j and x1+x2+…+xK=N should hold.
#
#You have to find the maximum possible value of the product (x21−x1)⋅(x22−x2)⋅…⋅(x2K−xK). Because this number could be huge, compute it modulo 109+7. If N cannot be represented as the sum of any K distinct positive integers, output −1 instead.


for _ in range(int(input())):
    n,k=map(int,input().split())
    ans=1
    temp=k*(k+1)>>1
    if n< temp:
        print(-1)
        continue
    temp=(n-temp)//k +1
    pat=[]
    sp=temp
    for i in range(k-1):
        pat.append(temp)
        temp+=1
    ep=(k)*(2*sp+k-1)//2
    temp+=n-ep
    pat.append(temp)
    fp=temp-(sp+(k-1))-1
    if k>1 and fp>0:
        pat[k-1]-=fp
        for i in range(k-2,-1,-1):
            if fp<=0:
                break
            pat[i]+=1
            fp-=1
    for i in range(k):
        har=(pat[i]*pat[i])%1000000007
        har=(har-pat[i]+1000000007)%1000000007
        ans=(ans*har)%1000000007
    print(int(ans))
