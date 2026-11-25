def solution(numbers) :
    result = []
    for number in numbers :
        bin_num = '0' + bin(number)[2:]
        n = len(bin_num)
        reverse_bin = list(bin_num[::-1])
        for i, (cur, nxt) in enumerate(zip(reverse_bin, reverse_bin[1:])) :
            if cur == '0' :
                reverse_bin[i] = '1'
                break
            if (cur, nxt) == ('1', '0') :
                reverse_bin[i], reverse_bin[i + 1] = '0', '1'
                break

        result.append(int(''.join(reversed(reverse_bin)), 2))
    
    return result