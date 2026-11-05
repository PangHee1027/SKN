import heapq


def solution(n, paths, gates, summits):
  summits_set = set(summits)
  gates_set = set(gates)
  summits.sort()
  graph = [[] for _ in range(n + 1)]

  for point1, point2, cost in paths:
    graph[point1].append((point2, cost))
    graph[point2].append((point1, cost))

  def dijkstra():
    intensity = [float('inf')] * (n + 1)
    hq = []
    for g in gates:
      intensity[g] = 0
      heapq.heappush(hq, (0, g))

    while hq:
      cur_cost, now = heapq.heappop(hq)

      if cur_cost > intensity[now]:
        continue

      if now in summits_set:
        continue

      for next_node, next_cost in graph[now]:
        if next_node in gates_set:
          continue
        cost = max(cur_cost, next_cost)
        if cost < intensity[next_node]:
          intensity[next_node] = cost
          heapq.heappush(hq, (cost, next_node))

    return intensity

  min_intensity, min_intensity_summit = float('inf'), 0
  intensities = dijkstra()
  for s in summits:
    if intensities[s] < min_intensity:
      min_intensity = intensities[s]
      min_intensity_summit = s

  return [min_intensity_summit, min_intensity]