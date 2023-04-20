# 11286_절댓값 힙
'''
- 배열에서 절댓값이 가장 작은 값을 출력하고, 배열에서 제거한다.
- 가장 작은 값이 여러 개일 때는 가장 작은 수 출력하고, 배열에서 제거한다.
'''

import heapq
import sys
input = sys.stdin.readline

N = int(input())
q = []

for x in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(q, (abs(x), x))  # 절댓값, 원래 값
    else:
        if q:   # 값이 있으면
            print(heapq.heappop(q)[1])  # 튜플로 담았으니까
        else:
            print(0)

'''
- 우선 순위 큐에 대한 기초 문제였던 거 같다.
- 덕분에 heapq 라는 모듈과 관련 메소드를 알게 된 시간이었다.
'''
