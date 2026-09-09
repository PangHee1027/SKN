input_int1 , input_int2 = input().split()
input_int1 , input_int2 = int(input_int1), int(input_int2)
result = input_int1 + input_int2

def is_even(i) :
    if (i % 2 == 0) :
        return "짝수"
    else :
        return "홀수" 
    
print(f"{is_even(input_int1)}+{is_even(input_int2)}={is_even(result)}")
