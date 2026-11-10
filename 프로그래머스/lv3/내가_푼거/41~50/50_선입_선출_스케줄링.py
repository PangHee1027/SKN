def solution(n, cores) :
    left, right = 0, max(cores) * n
    while left < right :
        mid = (left + right) // 2
        processing = len(cores) + sum(mid // x for x in cores)
        if processing >= n :
            right = mid
        else :
            left = mid + 1
    processed = len(cores) + sum((left - 1) // x for x in cores)

    for i, core in enumerate(cores):
      if left % core == 0:
        processed += 1
        if processed == n:
          return i + 1

print(solution(6, [1,2,3]))
    