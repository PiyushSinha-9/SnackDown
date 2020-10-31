#Snackdown 2019 is coming! Since Snackdown is a contest of teams with up to two members, everyone is looking for a teammate. There are N contestants (numbered 1 through N) who want to participate in Snackdown; let's denote the skill level of the i-th contestant by Si. These people want to pair up in N/2 teams; each team should consist of two people.
#
#Clearly everyone wishes for their teammate to be as skilled as possible, so everyone wants to maximize their teammate's skill level. We call a pairing (an unordered N/2-tuple of teams) valid if there are no two teams consisting of people (A,B) and (C,D) such that SD>SB and SA>SC — in that case, A and D would both prefer to be on the same team rather than with their current teammates.
#
#Find the number of valid pairings. Since this number can be large, compute it modulo 1,000,000,007.


import collections as cl
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a = sorted(a, reverse=True)
    b=dict(cl.Counter(a))
    temp=1
    flag=0
    flag2=0
    z1=0
    for i in b:
        z1+=b[i]
        if flag==1:
            temp=((temp%1000000007)*(b[i]%1000000007))%1000000007
            flag=0
        if flag2==1 and b[i]!=1:
            b[i]-=1
            flag2=0
        else:
            flag2=0
        if b[i]==1:
            temp*=1
        else:
            for i1 in range(1,b[i]+1,2):
                temp=((temp%1000000007)* (i1%1000000007))%1000000007
        if b[i] % 2 == 1 and z1%2!=0:
            flag2 = 1
            flag = 1
        else:
            flag = 0
    print(temp)
