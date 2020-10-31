#Chef has a sequence of positive integers A1,A2,…,AN. He has only one question for you: is it possible to change at most K elements of this sequence to arbitrary positive integers in such a way that the condition
#A21+A22+⋯+A2N≤A1+A2+⋯+AN

for _ in range(int(input())):
    f = list(map(int, input().split()))
    s = list(map(int, input().split()))
    count = 0
    for i in range(len(s)):
        if s[i] != 1:
            count += 1
    if f[1] >= count:
        print('YES')
    else:
        print('NO')
