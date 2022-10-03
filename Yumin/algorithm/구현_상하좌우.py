def solution():
    n= int(input())
    move= list(map(str, input().split()))

    p= [1, 1] #출발지
    for m in move:
        if m=='L':
            p[1]-=1 if p[1]-1>0 else 0
        elif m == 'R':
            p[1] += 1 if p[1]+1 < n+1  else 0
        elif m == 'U':s
            p[0] -= 1 if p[0]-1 > 0  else 0
        else: # m == 'D'
            p[0] += 1 if p[0]+1 < n+1  else 0

    print (p[0], p[1])

solution()