check_count = int(input())
check_list = input().split()

for i in range(len(check_list) - 1, -1, -1) :
    current_num = int(i) - 1
    print(check_list[i], end = " ")
