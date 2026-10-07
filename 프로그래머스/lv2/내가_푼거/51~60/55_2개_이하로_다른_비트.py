def solution(numbers):
    numbers = [bin(x)[2:].zfill(50) for x in numbers]
    answer = []

    for number in numbers :
        change = []
        reversed_number = list(reversed(number))
        reversed_number_pair = zip(reversed_number, reversed_number[1:])
        for i, (cur, next) in enumerate(reversed_number_pair) :
            if cur == "0" :
                change.append(i)
                break
            if (cur, next) == ("1", "0") :
                change.append(i)
                change.append(i + 1)
                break

        for i in change :
            reversed_number[i] = "1" if reversed_number[i] == "0" else "0"

        num = int("".join(reversed_number[::-1]), 2)
        answer.append(num)

    return answer

print(solution([2,7]))