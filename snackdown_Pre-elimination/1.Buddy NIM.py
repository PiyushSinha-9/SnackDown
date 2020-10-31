#Alice, Bob and Charlie are playing a new game called Buddy NIM. The game is played at two tables; on the first table, there are N heaps containing A1,A2,…,AN stones and on the second table, there are M heaps containing B1,B2,…,BM stones respectively.
#
#Initially, Alice is playing at the first table and Bob is playing at the second table. The players take their turns in this order: Charlie, Alice, Bob, Charlie, etc.
#
#Alice and Bob follow the rules for classical NIM - on Alice's turn, Alice must remove a positive number of stones from one of the piles at her current table and on Bob's turn, Bob must remove a positive number of stones from one of the piles at his current table. Whoever cannot remove any stone from a pile loses.
#
#Charlie does not play at any table. Instead, on his turn, he decides if Alice and Bob should keep playing at their respective tables or swap places.
#
#Alice and Charlie are buddies and they cooperate, playing in the optimal way that results in Alice's victory (if possible).
#
#It is clear that either Alice or Bob wins the game eventually. You must find out who the winner will be.
#
#


for _ in range(int(input())):
    n,m  = list(map(int,input().split()))
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    while(0 in a):
        a.remove(0)
    while(0 in b):
        b.remove(0)
    n = len(a)
    m = len(b)
    if(n!=m or sum(a)!=sum(b)):
        print("Alice")
    else:
        if(sorted(a)==sorted(b)):
            print("Bob")
        else:
            print("Alice")
