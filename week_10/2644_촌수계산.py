# 2644_촌수계산
'''
- 노드 저장할 graph 리스트 생성
- 방문 여부 판단할 visited 리스트 생성
- graph에 노드 저장
- dfs 함수 ㄱ
'''

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[0] * (n + 1) for _ in range(n + 1)]   # 가족 관계
visited = [0] * (n + 1)     # 방문 표시
ans = []

# 가족 관계 입력 받기
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v, cnt):
    cnt += 1        # 깊이가 깊어질 때 +1
    visited[v] = 1

    if v == b:
        ans.append(cnt)

    for i in graph[v]:
        if visited[i] == 0:
            dfs(i, cnt)

dfs(a, 0)

if len(ans) == 0:     # 여전히 0이면 연결 x
    print(-1)
else:
    print(ans[0] - 1)
