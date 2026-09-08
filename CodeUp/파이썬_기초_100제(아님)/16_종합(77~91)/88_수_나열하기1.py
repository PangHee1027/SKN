init_number , plus_number, repeat = input().split()
init_number , plus_number, repeat = int(init_number), int(plus_number), int(repeat)

def arithmetic_progression(a, d, n) :
    result = a
    for i in range(n - 1) :
        result += d
    return result

print(arithmetic_progression(init_number, plus_number, repeat))
