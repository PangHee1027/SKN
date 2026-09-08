check_count = int(input())
check_list = input().split()
result = 23

for i in check_list :
    current_num = int(i)
    if (current_num <= result) :
        result = current_num

print(result)
