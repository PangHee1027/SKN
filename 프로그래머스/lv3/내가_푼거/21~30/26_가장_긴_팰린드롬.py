import sys
sys.setrecursionlimit(100000)

def solution(s) :
    n = len(s)
    def palindrome_length(idx1, idx2) :
        result = 0
        if s[idx1] == s[idx2] :
            result += 2
        else :
            return 0
        next1, next2 = idx1 - 1, idx2 + 1
        if next1 < 0 or next2 >= n :
            return result
        result += palindrome_length(next1, next2)
        return result

    max_palindrome = 1

    for i, c in enumerate(s) :
        if i <= n - 2 and c == s[i + 1] :
            max_palindrome = max(max_palindrome, 2)
        next1, next2 = i - 1, i + 1
        if next1 < 0 or next2 >= n :
            continue
        max_palindrome = max(palindrome_length(next1, next2) + 1, max_palindrome)
        if c == s[next2] :
            next2 += 1
            if next2 >= n :
                continue
            max_palindrome = max(palindrome_length(next1, next2) + 2, max_palindrome)

    return max_palindrome

print(solution("abcdcba"))
print(solution("abacde"))