# 7576_토마토
'''
- 보관 후 하루가 지나면 익은 토마토 인접한 곳의 익지 않은 토마토가 익게 된다.
- 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향을 의미
- 며칠이 지나면 다 익게 되는지 최소 일수를 출력

- M : 상자 가로 칸의 수, N : 상자 세로 칸의 수
- 1 : 익은 토마토, 0은 익지 않은 토마토, -1: 빈 칸
- 저장될 때부터 모든 토마토가 익었다면 0 출력, 모두 익지 못하는 상황이면 -1 출력
'''

from pprint import pprint
from collections import deque

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

# 상, 하, 좌, 우
di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]

# 첫 토마토 위치
q = deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            q.append([i, j])


def bfs():
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if (0 <= ni < N) and (0 <= nj < M) and tomato[ni][nj] == 0:
                tomato[ni][nj] = tomato[i][j] + 1   # 1 더하면서 횟수 세기
                q.append([ni, nj])


ans = 0
bfs()
for x in tomato:
    for y in x:
        if y == 0:
            print(-1)
            exit()
    ans = max(ans, max(x))

# 첫 시작을 1로 했으니 빼줌
print(ans - 1)

'''
- 난 응용이 약하다... 그것은 내가 나약하기 때문인가...
- 오늘도 구선생님과 챗선생님과 함께 풀었음 담에 다시 풀기 도전
- 마지막 for문에서 break를 썼는데 틀렸고, exit()로만 고치니까 해결 됐음
- braek는 루프만 탈출되고, 등장하는 코드는 계속 실행됨! exit()는 강제 종료라는 걸 잊지 말길
'''
