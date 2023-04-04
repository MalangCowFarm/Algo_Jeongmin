# 1260_DFS와 BFS
'''
- 그래프를 첫째 줄에는 DFS, 다음 줄에는 BFS로 탐색한 결과 출력
- 방문할 수 있는 정점 여러 개인 경우 정점 번호가 작은 것 먼저 방문, 더 이상 방문할 수 없으면 종료
'''

from collections import deque
N, M, V = map(int, input().split())     # 정점, 간선, 탐색 시작점

matrix = [[0] * (N + 1) for _ in range(N + 1)]  # 인접 행렬

visited_d = [0] * (N + 1)       # dfs 방문한 곳 체크
visited_b = [0] * (N + 1)       # bfs 방문한 곳 체크

for _ in range(M):
    v1, v2 = map(int, input().split())
    matrix[v1][v2] = matrix[v2][v1] = 1     # 입력 받는 값에 대해 1 삽입

def dfs(V):
    visited_d[V] = 1      # 방문하는 곳에 1
    print(V, end=' ')

    for i in range(1, N + 1):
        if visited_d[i] == 0 and matrix[V][i] == 1:     # 방문 X, V와 연결 되어 있다면
            dfs(i)      # 더 깊이 탐색ㄱㄱ

def bfs(V):
    q = deque([V])
    visited_b[V] = 1    # v값 방문 처리

    while q:        # 큐 안에 데이터 없을 때까지
        V = q.popleft()     # 첫번째 값 꺼냄
        print(V, end=' ')
        for i in range(1, N + 1):
            if visited_b[i] == 0 and matrix[V][i] == 1:     # 방문 X, V와 연결 되어 있다면
                q.append(i)     # i값을 추가
                visited_b[i] = 1    # i값 방문 처리

dfs(V)
print()
bfs(V)
