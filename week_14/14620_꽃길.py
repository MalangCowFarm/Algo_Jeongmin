# 14620_꽃길
'''
- 꽃잎이 4개, 서로 겹치면 안됨 - 꽃 하나당 5평의 땅 대여
- 꽃잎이 핀 모양 기준으로 화단을 대여 해야 함
- 꽃을 심기 위해 필요한 최소 비용 출력 / 입력은 가격이 주어짐

* 풀이
- 5 * 5 로 모든 구역 방문 가능한지 체크
- 방문 가능하면 방문 표시하고 해당 구역에 있는 꽃 비용 누적
- 꽃 3개 선택 했을 때 비용이 최소인 경우 찾기
'''

N = int(input())
flower = [list(map(int, input().split())) for _ in range(N)]

di = [-1, 1, 0, 0, 0]
dj = [0, 0, -1, 1, 0]
visited = [[0 for _ in range(N)] for _ in range(N)]
ans = float('INF')


def check(r, c):    # 모든 구역 방문 가능한지
    global N
    for k in range(5):
        ni = r + di[k]
        nj = c + dj[k]
        if visited[ni][nj] or ni < 0 or ni > N - 1 or nj < 0 or nj > N - 1:
            return False
    return True


def dfs(r, cost, cnt):
    global ans
    if cnt == 3:
        ans = min(ans, cost)
        return

    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if check(i, j):     # 꽃을 심을 수 있을 때
                temp = 0
                for k in range(5):
                    ni = i + di[k]
                    nj = j + dj[k]
                    visited[ni][nj] = 1     # 방문 처리
                    temp += flower[ni][nj]
                dfs(i, cost + temp, cnt + 1)
                for k in range(5):
                    ni = i + di[k]
                    nj = j + dj[k]
                    visited[ni][nj] = 0     # 방문 회수

dfs(1, 0, 0)
print(ans)

'''
- 문제를 잘못 고른 거 같네요... 내가 골랐는데 내가 못 풀겠음...
- 죗옹합니다...ㅎ 전 구선생의 힘을 빌렸어요
'''
