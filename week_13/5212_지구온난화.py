# 5212_지구 온난화
'''
- R * C 그리드
- 50년 후, 인접한 3칸 or 4칸 잠김
- X : 땅, . : 바다
- 상,하,좌,우가 바다가 아닌 지점을 찾아야 함 -> 아닌 지점을 cnt += 1
'''

# 상, 하, 좌, 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]

for i in range(R):
    for j in range(C):
        cnt = 0
        if grid[i][j] == 'X':
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if ni < 0 or ni >= R or nj < 0 or nj >= C:
                    cnt += 1
                elif grid[ni][nj] == '.':
                    cnt += 1
            if cnt >= 3:
                grid[i][j] = '.'

'''
new_map = []
for i in grid:
    if 'X' in i:
        new_map.append(i)

- 새로운 지도를 어떻게 만들어야 하는지 모르겠숴요
'''