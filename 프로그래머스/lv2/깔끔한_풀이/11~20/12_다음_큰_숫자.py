def solution(n):
    target_count = bin(n).count("1")
    while True:
        n += 1
        if bin(n).count("1") == target_count:
            return n