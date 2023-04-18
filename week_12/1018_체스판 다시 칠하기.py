# 1018_체스판 다시 칠하기
'''
- N * M 크기의 보드 B W B W B | W B W B W
- 아무데서나 8 * 8 크기의 체스판으로 잘라낸 후 몇 개를 다시 칠해야 함
- 다시 칠해야 하는 정사각형의 최소 개수를 구하라...

- 완전 탐색으로 풀어야 하는 문제!
- 8 * 8 배열로 돌아 가면서 시작 점에 따라 옆에 와야 하는 게 다르기 때문에 고려 해야 함
- 바꿔야 하는 체스가 있다면 색칠한 후 += 1 개수 세기
- 그 중에 가장 작은 수를 출력할 것...
'''
from pprint import pprint

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

# 보드 다 돌면서 8 * 8 크기로 잘라 내야 함... 어떻게?...악악악!!!!!!!

ans = []
for i in range(N - 7):      # 범위 벗어 나는 거 방지 and 8 * 8씩 돌게 함
    for j in range(M - 7):
        b_cnt = 0       # 검은 색으로 시작
        w_cnt = 0       # 흰 색으로 시작

        for x in range(i, i + 8):       # 0~7
            for y in range(j, j + 8):
                if (x + y) % 2 == 0:
                    if board[x][y] == 'B':
                        w_cnt += 1      # w색으로
                    else:   # == 'W'
                        b_cnt += 1
                else:
                    if board[x][y] == 'B':
                        b_cnt += 1
                    else:
                        w_cnt += 1

        ans.append(b_cnt)
        ans.append(w_cnt)

print(min(ans))

'''
- 이게 실버 4면 난 브론즈가 확실하다
- 아직 완전 탐색에 대한 이해가 부족하다는 것을 깨닫게 됨
- 문제를 어떻게 접근해야 하는지는 알겠으나, 범위 설정에 대한 이해가 부족함
'''
