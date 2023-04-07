# 14938_서강그라운드
'''
- n : 지역의 개수, m : 수색범위, r : 길의 개수
- t : 각 구역에 있는 아이템의 수
- 플로이드-워셜 알고리즘
'''

N, M, R = map(int, (input().split()))
item = list(map(int, input().split()))
graph = [[1e9] * N for _ in range(N)]

for _ in range(R):
    s, e, d = map(int, (input().split()))
    graph[s-1][e-1] = min(graph[s-1][e-1], d)
    graph[e-1][s-1] = min(graph[e-1][s-1], d)

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            if i == j:
                graph[i][j] = 0

maxV = 0

for x in range(N):
    cnt = 0
    for y in range(N):
        if graph[x][y] <= M:
            cnt += item[y]

    maxV = max(maxV, cnt)

print(maxV)

'''
여전히 3중 for문에 대해 이해가 부족한 듯 싶습니다...
'''

