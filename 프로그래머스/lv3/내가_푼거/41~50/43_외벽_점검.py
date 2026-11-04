from itertools import permutations

def solution(n, weak, dist):
    checkpoint = len(weak)
    if checkpoint == 1 :
        return 1
    max_friends = len(dist)
    extended_weak = weak + [x + n for x in weak]
    for num_of_friends in range(1, max_friends + 1) :
        for permutation in permutations(dist, num_of_friends) :
            for i in range(checkpoint) :
                idx = i
                for x in permutation :
                    current = extended_weak[idx]
                    while idx < i + checkpoint and extended_weak[idx + 1] - current <= x:
                        idx += 1
                    idx += 1
                    if idx >= i + checkpoint:
                        break
                if idx >= i + checkpoint:
                    return num_of_friends

    return -1

print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))