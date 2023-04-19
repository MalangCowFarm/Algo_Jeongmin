# 3085_사탕 게임
'''
- N * N 배열
- 가로 or 세로 인접한 두 칸의 색을 바꿔서 먹을 수 있는 사탕의 최대 개수 구하는 것!
- C : 빨간색, P : 파란색, Z : 초록색, Y : 노란색

- 행과 열을 순회 하면서 연속된 같은 색상이 몇 개인지 체크
'''

def row_check():        # 행 체크
    global max_candy
    for i in range(N):
        cnt = 1
        for j in range(1, N):       # 범위 체크
            if candy[i][j] == candy[i][j - 1]:
                cnt += 1
            else:
                cnt = 1

            if cnt > max_candy:
                max_candy = cnt

def col_check():        # 열 체크
    global max_candy
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if candy[j][i] == candy[j - 1][i]:
                cnt += 1
            else:
                cnt = 1

            if cnt > max_candy:
                max_candy = cnt


N = int(input())
candy = [list(input()) for _ in range(N)]

max_candy = 1
for i in range(N):
    for j in range(N - 1):
        if candy[i][j] != candy[i][j + 1]:
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
            row_check()
            col_check()
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]

        if candy[j][i] != candy[j + 1][i]:
            candy[j][i], candy[j + 1][i] = candy[j + 1][i], candy[j][i]
            row_check()
            col_check()
            candy[j][i], candy[j + 1][i] = candy[j + 1][i], candy[j][i]

print(max_candy)

'''
- 범위... 설정... 아득하다
- 전역 변수가 헷갈렸는데 다시 알게 됨
'''
