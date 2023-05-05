# 1138_한 줄로 서기
'''
- 자신 보다 큰 사람이 왼쪽에 몇 명 있었는 지만 기억함
- 키가 1인 사람 부터 차례 대로 자신 보다 키가 큰 사람이 왼쪽에 몇 명 있는지 주어짐
- 줄을 선 순서 대로 키 출력

* 풀이
- 0으로 채워진 빈 리스트 생성
- 자신 보다 큰 사람 자리를 비워 두고 채우기
'''

N = int(input())
height = list(map(int, input().split()))

lst = [0] * N

for i in range(N):
    cnt = 0             # 큰 사람이 몇 명인지 0의 개수로 판단
    for j in range(N):
        if height[i] == cnt and lst[j] == 0:
            lst[j] = i + 1
            break
        elif lst[j] == 0:       # 빈 자리인 경우
            cnt += 1

print(*lst)
