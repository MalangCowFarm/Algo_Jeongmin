# 2615_오목
'''
- 구현, 브루트포스 알고리즘
- 검은 돌 : 1, 흰 돌 : 2, 무승부 : 0
- 가로, 세로, 대각선으로 같은 색 돌 5개 - 6개 이상은 이긴 거 X
- 이긴 돌의 가로 줄(행) 번호, 세로 줄(열) 번호 순서 대로 출력

- 오른쪽, 아래쪽, 오른쪽 아래, 왼쪽 아래 - 델타 이용
'''

N = 19
board = [list(map(int, input().split())) for _ in range(N)]

# 오른쪽, 오른쪽 아래, 아래쪽, 왼쪽 아래 (시계 방향)
di = [0, 1, 1, 1]
dj = [1, 1, 0, -1]

find = False

def check():
    global find

    for i in range(N):
        for j in range(N):

            if board[i][j] != 0:
                target = board[i][j]    # 위치

                for k in range(4):
                    cnt = 1

                    # 바둑알 위치
                    ni = i + di[k]
                    nj = j + dj[k]

                    while 0 <= ni < N and 0 <= nj < N and board[ni][nj] == target:
                        cnt += 1
                        if cnt == 5:
                            # 육목 판정
                            if 0 <= i - di[k] < 19 and 0 <= j - dj[k] < 19 \
                                    and board[i - di[k]][j - dj[k]] == target:
                                break
                            if 0 <= ni + di[k] < 19 and 0 <= nj + dj[k] < 19 \
                                    and board[ni + di[k]][nj + dj[k]] == target:
                                break

                            print(target)
                            print(i + 1, j + 1)
                            find = True
                            return

                        # 위치 업데이트
                        ni += di[k]
                        nj += dj[k]

    if (find == False):
        print(0)
        return

check()

'''
- 구현이 아직 많이 부족하다는 걸 다시 깨닫게 됨
- 아니 근데...
- 육목 판정이 어려웠음... 그래서 구선생 참고함...
'''