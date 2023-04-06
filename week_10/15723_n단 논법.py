# 15723_n단 논법
'''
- 플로이드-워셜 알고리즘: 최단 경로(길찾기) 알고리즘 중 하나
- 모든 노드 간의 최단 경로를 계산할 때 사용하는 알고리즘임
- 직접적으로 연결되어 있지 않으면 무한대(inf)로 선언, 자기 자신은 0으로 초기화

- 입력 어떻게 받아야 할지 고민... -> 문자를 숫자로 치환해야 함 ;;
- 무한(inf)의 값으로 1e9 이용...(10억 이내)
'''

N = int(input())
graph = [[1e9 for _ in range(26)] for _ in range(26)]   # 알파벳 26개
for _ in range(N):
    txt = input().split()
    s = ord(txt[0]) - ord('a')  # 숫자로 치환
    e = ord(txt[2]) - ord('a')
    graph[s][e] = 1     # 1로 변경

# 플로이드-워셜...
for k in range(26):
    for i in range(26):
        for j in range(26):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

M = int(input())
for _ in range(M):
    txt = input().split()
    s = ord(txt[0]) - ord('a')
    e = ord(txt[2]) - ord('a')

    if graph[s][e] < 1e9:   # 갈 수 있는 거리에 해당하면
        print('T')
    else:
        print('F')

'''
- 플로이드-워셜이 뭔지 이해를 못 하겠음
- 이중 for문도 이해 하기 힘들어 하는데... 삼중 for문?...
'''
