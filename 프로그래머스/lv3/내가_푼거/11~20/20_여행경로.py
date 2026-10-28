import sys
sys.setrecursionlimit(100000)

def solution(tickets):
    n = len(tickets) + 1
    tickets.sort()

    def dfs(cur_visited, remain) :
        if len(cur_visited) == n :
            return cur_visited
        last_visit = cur_visited[-1]
        stack = []
        for i, ticket in enumerate(remain) :
            departure, arrival = ticket
            if departure == last_visit :
                next_visited = cur_visited + [arrival]
                next_remain = stack + remain[i + 1:]
                cur_result = dfs(next_visited, next_remain)
                if cur_result :
                    return cur_result
            stack.append([departure, arrival])
        return []
    
    stack = []
    for i, ticket in enumerate(tickets) :
        departure, arrival = ticket
        if departure == 'ICN' :
            next_visited = [departure, arrival]
            next_remain = stack + tickets[i + 1:]
            result = dfs(next_visited, next_remain)
            if result :
                return result
        stack.append([departure, arrival])

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])) # ["ICN", "JFK", "HND", "IAD"]
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])) # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]