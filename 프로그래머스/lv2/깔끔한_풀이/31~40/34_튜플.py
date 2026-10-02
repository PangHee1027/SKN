def solution(s):
    # 1. 문자열 파싱
    s = s.replace("{{", "").replace("}}", "")
    ls = s.split("},{")
    ls = [list(map(int, l.split(","))) for l in ls]
    
    # 2. 길이 순 정렬
    ls.sort(key=len)
    
    answer = []
    visited = set()  # 탐색 속도 O(1)을 위한 set
    
    # 3. 차례대로 확인하며 새로운 원소 추가
    for l in ls:
        for x in l:
            if x not in visited:
                answer.append(x)
                visited.add(x)
                break  # 각 집합당 새로 추가되는 원소는 1개뿐이므로 탐색 종료
                
    return answer