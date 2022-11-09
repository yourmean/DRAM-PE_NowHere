import sys
input = sys.stdin.readline

# 거리 계산
def distance():
    global ans
    total_dist = 0
    for x, y in home:
        tmp = int(1e9)
        for px, py in pick: tmp = min(tmp, abs(px-x)+abs(py-y))
        total_dist += tmp
    ans = min(ans, total_dist)
    
# 치킨집 pick
def pickchic(idx, cnt):
    global length
    if cnt == m:
        distance()
        return
    for c in range(idx, length):
        pick.append(chic[c])
        pickchic(c+1, cnt+1)
        pick.remove(chic[c])

n, m = map(int, input().split())
zido = []
chic = []
home = []
pick = []

for i in range(n):
    zido.append(list(map(int, input().split())))
    for j in range(n):
        if zido[i][j] == 1: home.append((i, j))
        elif zido[i][j] == 2: chic.append((i, j))
length = len(chic)
ans = int(1e9)

pickchic(0, 0)
print(ans)
