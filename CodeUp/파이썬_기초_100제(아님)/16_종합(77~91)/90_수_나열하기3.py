init_number , multi_number, plus_number, repeat = input().split()
init_number , multi_number, plus_number, repeat = int(init_number), int(multi_number), int(plus_number), int(repeat)

def special_sequence(a, m, d, n) :
    result = a
    for i in range(n - 1) :   
        result *= m
        result += d
    return result

print(special_sequence(init_number, multi_number, plus_number, repeat))
