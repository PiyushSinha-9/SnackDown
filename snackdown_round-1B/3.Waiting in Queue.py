#Chef has opened his new restaurant and made the first meal free for everyone!
#
#You want to try the new restaurant, but since it is offering free meals, many people are coming and a huge queue has formed. Currently (at time T=0), there are M people waiting in the queue. You also know that there are N more people coming; let's denote the time when the i-th person stands at the back of the queue by Ai. You noticed that each exactly L seconds, one place in the restaurant will become vacant and the person currently at the front of the queue takes it, i.e. at time T=L, one person enters, then at time T=2L, another person enters and so on.
#
#You do not like to wait in queues, so you want to choose the time when you stand at the back of the queue in such a way that the time between this moment and the moment when you enter the restaurant is minimum possible. Assume that if you decide to stand at the back of the queue at the same moment as some other person, you will stand before them in the queue (closer to the restaurant). Also, you have to stand at the back of the queue no later than in the K-th second, otherwise you will arrive at home late.
#
#What is the minimum time you have to spend standing in the queue?

for y in range(int(input())):
    n,m,k,l=map(int, input().split())
    arr=list(map(int, input().split()))
    arr=sorted(arr)
    mini=(m+1)*l-(1%l)
    for i in range(n):
        s=m-(arr[i]//l)+i
        s=(s+1)*l-(arr[i]%l)
        if s<mini:
            mini=s
    s=m-(k//l)+n
    s=(s+1)*l-(k%l)
    if s<mini:
        mini=s
    print(mini)
