from collections import deque


def bfs(start, ignore_node, graph, n):
  """BFS(너비 우선 탐색)를 통해 끊어진 간선을 제외하고 연결된 송전탑(노드)의 개수를 세는 함수

  :param start: 탐색을 시작할 송전탑 번호
  :param ignore_node: 끊어진 간선으로 연결된 반대쪽 송전탑 번호 (방문 제외 대상)
  :param graph: 인접 리스트 형식의 전력망 그래프
  :param n: 전체 송전탑 개수
  :return: start 송전탑과 연결된 전력망의 총 송전탑 개수
  """
  # 노드 번호가 1부터 n까지이므로 (n + 1) 크기의 방문 여부 배열 생성
  visited = [False] * (n + 1)

  # 시작 노드 방문 처리 및 큐 초기화
  visited[start] = True
  queue = deque([start])

  # 시작 노드 자기 자신을 포함하여 연결된 노드 개수 1부터 카운트
  count = 1

  while queue:
    node = queue.popleft()

    # 현재 노드와 인접한 다른 노드들을 확인
    for nxt in graph[node]:
      # 끊어진 간선의 반대쪽 노드(ignore_node)이거나 이미 방문한 노드라면 건너뜀
      if nxt != ignore_node and not visited[nxt]:
        visited[nxt] = True  # 방문 표시
        queue.append(nxt)  # 다음 탐색을 위해 큐에 삽입
        count += 1  # 연결된 송전탑 개수 증가

  return count


def solution(n, wires):
  # 1. 인접 리스트(Adjacency List) 방식으로 무방향 그래프 구축
  # 1번부터 n번 송전탑까지 사용하기 위해 (n + 1) 개의 빈 리스트 생성
  graph = [[] for _ in range(n + 1)]

  for v1, v2 in wires:
    # 양방향 연결 정보 추가
    graph[v1].append(v2)
    graph[v2].append(v1)


  # 두 전력망의 송전탑 개수 차이의 최솟값을 저장할 변수 (최댓값인 n으로 초기화)
  answer = n

  # 2. 주어진 모든 전선(간선)을 하나씩 끊어보며 완전탐색(Brute-force) 진행
  for v1, v2 in wires:
    # v1과 v2를 연결하는 전선을 끊었다고 가정하고,
    # v1에서 출발하여 v2 방향으로 가가지 않는(ignore_node=v2) 송전탑 개수를 측정
    cnt = bfs(v1, v2, graph, n)

    # 한쪽 전력망의 송전탑 개수가 cnt이면, 반대쪽 전력망은 (n - cnt)개가 됨
    # 두 전력망 개수 차이: |cnt - (n - cnt)| = |2 * cnt - n|
    diff = abs(2 * cnt - n)

    # 이전까지의 최솟값과 비교하여 더 작은 차이 값으로 갱신
    answer = min(answer, diff)

  return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))