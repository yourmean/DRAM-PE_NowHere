#https://www.acmicpc.net/problem/18352

from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
a, b, c, d = map(int, input().split())
graph = [[] for _ in range(a + 1)]

# 모든 도로정보 입력받기
for _ in range(b):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단거리 초기화
distance = [-1] * (a+1)
distance[d] = 0 # 출발 도시까지의 거리 = 0으로 설정

# BFS 수행
q = deque([d])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시인 경우 최단 거리 갱신
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
target = False
for i in range(1, a+1):
    if distance[i] == c:
        print(i)
        target = True

# 최단 거리가 K인 도시가 없는 경우
if target == False:
    print(-1)
