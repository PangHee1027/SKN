def solution(a, b):
    date = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    convert = sum(day[:a - 1]) + b
    return date[convert % 7]