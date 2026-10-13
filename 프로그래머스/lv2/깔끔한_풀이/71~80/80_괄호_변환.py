def check(string):
    count = 0
    for s in string:
        if s == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    return True

def divide(p):
    count = 0
    for i, s in enumerate(p):
        if s == "(":
            count += 1
        else:
            count -= 1
        # 괄호 특성상 첫 글자에서 바로 0이 될 수 없으므로 i > 0은 생략 가능합니다.
        if count == 0:
            return p[:i + 1], p[i + 1:]

def solution(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if not p:
        return ""
    
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
    u, v = divide(p)
    
    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면
    if check(u):
        # u에 v를 1단계부터 다시 수행한 결과를 이어 붙임
        return u + solution(v)
    
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면
    else:
        result = ["("]
        result.append(solution(v))
        result.append(")")
        
        # u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집음
        reversed_u = ["(" if s == ")" else ")" for s in u[1:-1]]
        result.extend(reversed_u)
        
        return "".join(result)