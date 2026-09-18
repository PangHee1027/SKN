def solution(s):
    num_dict = {'zero' : 0, 'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9}
    stack = []
    answer = []
    for i in range(len(s)) :
        stack.append(s[i])
        current = "".join(stack)
        if current in num_dict :
            answer.append(str(num_dict[current]))
            stack = []
        elif current in list(map(str, range(10))) :
            answer.append(str(current))
            stack = []

    return int("".join(answer))

# print(solution("123"))