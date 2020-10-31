#Chef has two sequences A and B, each with length N. He can apply the following magic operation an arbitrary number of times (including zero): choose an index i (1≤i≤N−2) and add 1 to Ai, 2 to Ai+1 and 3 to Ai+2, i.e. change Ai to Ai+1, Ai+1 to Ai+1+2 and Ai+2 to Ai+2+3.
#
#Chef asks you to tell him if it is possible to obtain sequence B from sequence A this way. Help him!
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(n-2):
        diff = b[i] - a[i]
        if diff > 0:
            a[i] += diff
            a[i+1] += 2*diff
            a[i+2] += 3*diff
        elif diff < 0:
            break
        else:
            continue

if a == b:
    print("TAK")
    else:
        print("NIE")
