import collections

def solution(want, number, discount):
    want_dict = dict(zip(want, number))
    count = 0
    for i in range(len(discount)) :
        if len(discount) - i < sum(number) :
            break
        compare_dict = collections.Counter(discount[i:i + sum(number)])
        if want_dict == compare_dict :
            count += 1
    return count

# print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))