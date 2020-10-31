#Chef has a difficult problem to solve. He has N segments [l1,r1],[l2,r2],…,[lN,rN] on the x-axis. A K-subset of these N segments consists of any K of these segments. For each K-subset, consider the common intersection of all the K segments, i.e. the set of points which belong to each of the K segments. The intersection of segments is also a segment; the length of a segment [l,r] is r−l. Chef is asking you to find the maximum of lengths of the common intersections in all K-subsets



import heapq
def solve():
    a = 0
    for i in range(k-1,n):
        m = heapq.heappushpop(h,a[i][1])
        a = max(max(0,m - a[i][0]), a)
    return a

for _ in range(int(input())):
    n,k = [int(x) for x in input().split()]
    a = []
    for i in range(n):
        a.append([int(x) for x in input().split()])
    a.sort()
    h = []
    for i in range(k-1):
        heapq.heappush(h,a[i][1])
    print(solve())
