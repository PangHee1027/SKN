def day_of_week(offset):
    return (5 + offset - 1) % 7

day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def sum_of_month(i) : 
    sum = 0
    for j in range(i - 1) :
        sum += month[j]
        print(month[j])
    return sum

def solution(a, b):
    answer = day[day_of_week(sum_of_month(a) + b)]
    return answer

print(solution(1, 1))
