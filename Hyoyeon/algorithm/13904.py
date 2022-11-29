#단 가장 높은 점수부터, 최대 미룰수있는 날짜에 매칭한다
#그 다음 높은 점수를, 가능한 가장 느린 날에 놓는다
#그 다음 높은 점수의 가장 마지막날에 이미 있으면, 그 전날에 둔다
#둘 곳이 없으면 이보다 작은 점수로 간다 

import sys
n = int(sys.stdin.readline())
homeworks = []
visit = [False] * 1001

for _ in range(n):
    d, s = map(int, sys.stdin.readline().split())
    homeworks.append((d, s))

homeworks.sort(key=lambda x: x[1], reverse=True)
answer = 0
for day, score in homeworks:
    i = day
    # 과제를 할 날짜 탐색
    while i > 0 and visit[i]:
        i -= 1
    # 과제를 할 날짜가 없으면 패스
    if i == 0:
        continue
    else:
        visit[i] = True
        answer += score

print(answer)
