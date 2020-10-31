#Chef got in the trouble! He is the king of Chefland and Chessland. There is one queen in Chefland and one queen in Chessland and they both want a relationship with him. Chef is standing before a difficult choice…
#
#Chessland may be considered a chessboard with N rows (numbered 1 through N) and M columns (numbered 1 through M). Let's denote a unit square in row r and column c by (r,c). Chef lives at square (X,Y) of this chessboard.
#
#Currently, both queens are living in Chessland too. Each queen, when alone on the chessboard, can see all squares that lie on the same row, column or diagonal as itself. A queen from (xq,yq) cannot see a square (r,c) if the square (X,Y) is strictly between them. Of course, if the queens can see each other, the kingdom will soon be in chaos!
#
#Help Chef calculate the number of possible configurations of the queens such that the kingdom will not be in chaos. A configuration is an unordered pair of distinct squares (xq1,yq1) and (xq2,yq2) such that neither of them is the square (X,Y). Two configurations are different if the position of queen 1 is different or the position of queen 2 is different.


import sys
inp = sys.stdin.read().strip()

def choose2(n):
    return n*(n-1)/2

def solve(n,m,x,y):
    count = n*choose2(m) + m*choose2(n)
    count
    small = min(n,m)
    big = max(n,m)
    
    diags = (big-small+1)*choose2(small)
    for i in range(2,small,1):
        diags += 2*choose2(i)
    
    diags
    count += 2*diags
    
    count
    valid = choose2(n*m)-count
    valid
    a = x-1
    b = min(x-1,y-1)
    c = y-1
    e = n-x
    d = min(c,e)
    g = m-y
    h = min(a,g)
    f = min(e,g)
    
    valid -= n*m - (a+b+c+d+e+f+g+h) - 1
    valid
    valid += (a*e)+(b*f)+(c*g)+(d*h)
    
    print(int(valid*2))

lines = inp.split("\n")
for line in lines[1:]:
    n,m,x,y = [int(a) for a in line.strip().split(" ")]
    solve(n,m,x,y)
