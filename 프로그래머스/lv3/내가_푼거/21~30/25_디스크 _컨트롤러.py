import heapq

def solution(jobs):
    jobs.sort(key = lambda x : x[0], reverse = True)
    heap = []
    finish = []
    job_idx = 0
    n = len(jobs)
    time = 0

    cur_job = 0
    while len(finish) < n :
        if not cur_job and heap :
            r, s, _ = heapq.heappop(heap)
            cur_job = [r, s]
        while jobs and jobs[-1][0] == time :
            start, require = jobs.pop()
            heapq.heappush(heap, (require, start, job_idx))
            job_idx += 1
        if cur_job :
            cur_job[0] -= 1
            if not cur_job[0] :
                finish.append(time - cur_job[1])
                cur_job = 0
        time += 1

    return sum(finish) // n

print(solution([[0, 3], [1, 9], [3, 5]])) # 8