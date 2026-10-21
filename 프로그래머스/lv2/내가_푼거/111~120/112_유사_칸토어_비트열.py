import sys

sys.setrecursionlimit(10000000)

def solution(n, l, r):
    def cantore(num, indices) :
        if num == 0 :
            return 0
        
        if indices == 0 :
            return 1

        block_size = (5 ** (indices - 1))
        panel = num // block_size
        num_of_1_in_panel = 4 ** (indices - 1)
        if panel == 5 :
            return 4 * num_of_1_in_panel
        
        count_one = [0, num_of_1_in_panel, 2 * num_of_1_in_panel, 2 * num_of_1_in_panel, 3 * num_of_1_in_panel]
        num -= block_size * panel
            
        return count_one[panel] + (cantore(num, indices - 1) if panel != 2 else 0)
    
    return cantore(r, n) - cantore(l - 1, n)


print(solution(2, 4, 17))