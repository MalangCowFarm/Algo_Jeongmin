# 1992_쿼드트리
'''
- 4개로 쪼개는 것은 2630번 문제와 동일
- 괄호를 어떻게 출력해야 할지 고민해볼 것...
'''

N = int(input())
board = [list(map(int, input())) for _ in range(N)]
ans = ''

def check(x, y, n):
    global ans
    video = board[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if video != board[i][j]:
                ans += '('
                half = n // 2
                check(x, y, half)  # 1사분면
                check(x, y + half, half)  # 2사분면
                check(x + half, y, half)  # 3사분면
                check(x + half, y + half, half)  # 4사분면
                ans += ')'
                return

    if video == 0:
        ans += '0'
    else:
        ans += '1'

check(0, 0, N)

print(ans)

'''
- 2630번 풀고 푸니까 연관 되어 있어서 괜찮았는 듯 합니다.
- 괄호가 어디에 들어 갈지만 고려하면 됐었음
'''
