# 2594_놀이공원
'''
- 운행 일정을 시간 단위로 변환함 - 시작, 종료 시간 분 단위로 계산
- 시간 순으로 정렬하기
- 시작 시간, 종료 시간 사이에 쉴 수 있는 시간 구하기
'''

time = [[600, 600], [1320, 1320]]
N = int(input())

for _ in range(N):
    x, y = input().split()
    x = int(x[:2]) * 60 + int(x[2:]) - 10
    y = int(y[:2]) * 60 + int(y[2:]) + 10
    time.append([x, y])
time.sort()

rest = 0
last = 600      # 10시로 초기화

for s, e in time:
    rest = max(rest, s - last)  # 시작 시간 - 이전 놀이기구에서 탄 시각
    last = max(last, e)         # 이전 놀이기구에서 탄 시각, 종료 시간

print(rest)


'''
- 잘 모르겠어요... 여전히... 시간 계산에 약합니다
'''
