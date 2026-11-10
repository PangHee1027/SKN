n = int(input())

float_list = []

for _ in range(n) :
    float_list.append(float(input()))

for i in range(1, n) :
    float_list[i] = max(float_list[i], float_list[i - 1] * float_list[i])

print(f'{max(float_list):.3f}')