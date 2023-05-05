# 1697_숨바꼭질
'''
- 수빈이가 X일 때 걷는다면 1초 후에 X - 1, X + 1, 2 * X 의 위치로 이동함
- 수빈이가 동생을 찾을 수 있는 가장 빠른 시간 몇 초 후인지 출력

* 풀이
- bfs 활용
'''

from collections import deque


def bfs(v):
    q = deque([v])

    while q:
        v = q.popleft()
        if v == K:
            return lst[v]
        for next_v in (v - 1, v + 1, 2 * v):    # 이동할 수 있는 경우
            if 0 <= next_v < MAX and not lst[next_v]:
                lst[next_v] = lst[v] + 1    # 초기화
                q.append(next_v)


MAX = 100001
N, K = map(int, input().split())
lst = [0] * MAX     # 최소 시간 저장, v에서 부터 최소 이동 횟수 저장 되어 있음
print(bfs(N))
