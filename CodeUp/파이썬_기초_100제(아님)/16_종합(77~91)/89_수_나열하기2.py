init_number , multi_number, repeat = input().split()
init_number , multi_number, repeat = int(init_number), int(multi_number), int(repeat)

def geometric_progression(a, r, n) :
    result = a
    for i in range(n - 1) :
        result *= r
    return result

print(geometric_progression(init_number, multi_number, repeat))
