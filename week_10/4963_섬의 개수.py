# 4963_섬의 개수
'''
- 1 = land, 0 = sea
- 가로, 세로, 대각선으로 연결되어 있으면 하나의 섬이라고 볼 수 있음
- 지도는 바다로 둘러 쌓여 있음 (0으로 둘러 쌓여 있다고 보면 됨)
'''

from collections import deque

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(x, y):
    visited[x][y] = 1
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()

        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < h and 0 <= ny < w:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = 1
                    q.append((nx, ny))


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = []
    visited = [[0] * w for _ in range(h)]
    ans = 0

    for _ in range(h):
        graph.append(list(map(int, input().split())))

    for x in range(h):
        for y in range(w):
            if graph[x][y] == 1 and not visited[x][y]:
                bfs(x, y)
                ans += 1

    print(ans)
