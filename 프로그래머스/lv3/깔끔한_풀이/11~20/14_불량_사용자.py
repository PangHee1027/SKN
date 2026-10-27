def is_ban(user, banned):
    if len(user) != len(banned):
        return False
    return all(s2 == '*' or s1 == s2 for s1, s2 in zip(user, banned))

def solution(user_id, banned_id):
    visited = set()
    n = len(banned_id)

    def dfs(banned_idx, current_set):
        # 모든 banned_id에 대한 매칭을 완료한 경우
        if banned_idx == n:
            visited.add(frozenset(current_set))
            return
        
        banned = banned_id[banned_idx]
        for uid in user_id:
            # 이미 사용한 아이디가 아니고, 조건에 부합한다면
            if uid not in current_set and is_ban(uid, banned):
                current_set.add(uid)
                dfs(banned_idx + 1, current_set)
                current_set.remove(uid)  # 백트래킹 (원상복구)

    dfs(0, set())
    return len(visited)