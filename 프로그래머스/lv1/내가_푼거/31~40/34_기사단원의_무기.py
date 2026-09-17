def solution(number, limit, power):
    answer = 0

    for i in range(1, number + 1) :
        count = 0
        for j in range(1, int(i**(1/2))+1) :
            if i % j == 0  :
                count += 1 
                if j < i // j :
                    count += 1

        answer += count if count <= limit else power
    return answer

# print(solution(10, 3, 2))