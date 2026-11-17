def solution(answers):
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    result = [0, 0, 0]
    for i, answer in enumerate(answers) :
        if answer == supo1[i % 5] :
            result[0] += 1
        if answer == supo2[i % 8] :
            result[1] += 1
        if answer == supo3[i % 10] :
            result[2] += 1
    return sorted([i + 1 for i, x in enumerate(result) if x == max(result)])