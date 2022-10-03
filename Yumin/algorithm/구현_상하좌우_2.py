def solution():
    n = int(input())
    plan = input().split()

    x, y = 1, 1  # 출발지
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    type = ['L', 'R', 'U', 'D']

    for p in plan:
        for i in range(len(type)):
            if plan == type[i]:
                nx = x + dx[i]
                ny = y + dy[i]
            if nx < 1 or nx > n or ny < 1 or ny > n:
                continue
            x, y = nx, ny

    print(x, y)


solution()