#Snackdown 2019 is coming! People have started to spread the word and tell other people about the contest.
#
#There are N people numbered 1 through N. Initially, only person 1 knows about Snackdown. On each day, everyone who already knows about Snackdown tells other people about it. For each valid i, person i can tell up to Ai people per day. People spread the information among the people who don't know about Snackdown in the ascending order of their indices; you may assume that no two people try to tell someone about Snackdown at the same moment. Each person is only allowed to start telling other people about Snackdown since the day after he/she gets to know about it (person 1 can start telling other people already on day 1). How many days does it take for all people to know about Snackdown?

for _ in range(int(input())):
    a=int(input())
    b=list(map(int,input().split()))
    j=0
    i=1
    t1=0
    c=0
    t=0
    while i<a:
        t1=sum(b[j:i])
        t+=t1
        j=i
        i+=t
        c+=1
    print(c)
