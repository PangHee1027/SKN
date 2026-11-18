def solution(numbers, hand) :
    keypad = {1 : (0, 0), 2 : (0, 1), 3 : (0, 2), 4 : (1, 0), 5 : (1, 1), 6 : (1, 2),
             7 : (2, 0), 8 : (2, 1), 9 : (2, 2), '*' : (3, 0), 0 : (3, 1), '#' : (3, 2)
             }
    l = "*"
    r = '#'
    answer = ''
    for n in numbers :
        if n in (1, 4, 7) :
            answer += 'L'
            l = n
        elif n in (3, 6, 9) :
            answer += 'R'
            r = n
        else :
            l_d = sum(abs(a - b) for a, b in zip(keypad[n], keypad[l]))
            r_d = sum(abs(a - b) for a, b in zip(keypad[n], keypad[r]))
            if l_d > r_d :
                answer += 'R'
                r = n
            elif l_d < r_d :
                answer += 'L'
                l = n
            else :
                if hand == 'right' :
                    answer += 'R'
                    r = n
                else :
                    answer += 'L'
                    l = n
            
    return answer