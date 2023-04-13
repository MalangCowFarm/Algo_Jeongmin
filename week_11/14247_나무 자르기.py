# 14247_나무 자르기
'''
- 그리디 알고리즘 : 각 단계에서 최적의 선택을 함. 단, 최종 결과가 최적해라는 보장 X
- 나무를 잘라서 구할 수 있는 최대 양 출력
- n일 동안 n개 나무, 0부터 다시 자리기 때문에 같은 나무 여러 번 자를 수 있음

- 첫 날 나무 길이랑 자라는 속도 묶기
- 처음에 베어야 하는 나무를 자라나는 속도가 가장 빠른 나무로 베어야 함!!
'''

N = int(input())

height = list(map(int, input().split()))    # 첫 날 올라 갔을 때 나무 길이
speed = list(map(int, input().split()))     # 나무들이 자라는 길이

trees = []
for i in range(N):
    trees.append([height[i], speed[i]])

trees = sorted(trees, key=lambda x: x[1])

ans = 0
for t in range(N):
    ans += trees[t][0] + (t * trees[t][1])

print(ans)

'''
- 나무 길이와 자라는 속도를 묶는 것까지는 생각했으나...
- 처음에 단! 한 개의 나무만 벨 수 있는 줄 알고 시간 낭비함...
'''
