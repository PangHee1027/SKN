student_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
check_count = int(input())
check_list = input().split()

for i in check_list :
    current_num = int(i) - 1
    student_list[current_num] += 1

for i in student_list :
    print(i, end = " ")
