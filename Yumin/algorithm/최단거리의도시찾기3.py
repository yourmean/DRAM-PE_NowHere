import sys
from collections import deque

# 도시 수, 도로 수, 거리정보, 출발도시 번호
city, road, dist, start = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(city + 1)]
distance = [0] * (city+1)
visit = [False] * (city+1)

# 도로정보
for _ in range(road):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)


ans = []
queue = deque([start])
visit[start] = True

# bfs 수행
while queue:
    start = queue.popleft()
    for i in graph[start]:
        if not visit[i]:
            queue.append(i)
            visit[i] = True
            distance[i] = distance[start] + 1
            if distance[i] == dist:
                ans.append(i)

# 최단거리=k인 도시가 없는 경우
if len(ans) == 0: 
    print(-1)

# 최단거리=k인 모든 도시 오름차순 출력
else:
    ans.sort()
    for i in range(len(ans)):
        print(ans[i])
