# 2630_색종이 만들기
'''
- 하얀색 0, 파란색 1
- 색상이 모두 같지 않은 경우 4개로 쪼개서 재귀... -> 쿼드 트리라고 한다고 함
- 만족하는 경우 해당 값 카운팅
'''

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

white, blue = 0, 0

def check(x, y, n):
    global white, blue
    color = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != paper[i][j]:
                half = n // 2
                check(x, y, half)      # 1사분면
                check(x, y + half, half)     # 2사분면
                check(x + half, y, half)     # 3사분면
                check(x + half, y + half, half)    # 4사분면
                return

    if color == 0:
        white += 1
    else:
        blue += 1


check(0, 0, N)

print(white)
print(blue)

'''
- 분할 정복이 초면이라... 풀이 참고해서 이해했습니다.
'''
