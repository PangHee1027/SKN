from itertools import permutations

def solution(numbers):
    numbers_list = list(numbers)
    numbers_comb = []
    created_numbers = set()
    for i in range(1, len(numbers_list) + 1) :
        numbers_comb += list(permutations(numbers_list, i))

    for nc in numbers_comb :
        created_numbers.add(int("".join(nc)))
    
    answer = 0

    for number in list(created_numbers) :
        if number == 1 or number == 0 :
            continue
        root_number = int(number ** 0.5)
        for i in range(2, root_number + 1) :
            if number % i == 0 :
                break
        else :
            answer +=1

    return answer

print(solution("17"))