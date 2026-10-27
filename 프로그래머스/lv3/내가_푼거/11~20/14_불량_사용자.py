def is_ban(user, banned) :
    n = len(user)

    if n != len(banned) :
        return False
    
    for i, zip_str in enumerate(zip(user, banned)) :
        s1, s2 = zip_str
        if s2 == "*" :
            continue
        if s1 != s2 :
            return False

    return True

def solution(user_id, banned_id):
    visited_state = []
    n = len(banned_id)

    def dfs(user, banned, state) :
        result = 0
        if is_ban(user, banned) :
            next_state = state.union({user})
            if len(next_state) == n :
                if next_state not in visited_state :
                    visited_state.append(next_state)
                return
            for uid in user_id :
                if uid in next_state :
                    continue
                dfs(uid, banned_id[len(next_state)], next_state)
        return

    for uid in user_id :
        result = dfs(uid, banned_id[0], set())

    return len(visited_state)

#print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])) # 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])) # 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])) # 3