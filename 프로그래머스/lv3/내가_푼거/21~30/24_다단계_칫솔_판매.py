def solution(enroll, referral, seller, amount):
    n = len(enroll)
    enroll_idx = {x : i for i, x in enumerate(enroll)}
    enroll_parent = {x : y if y != '-' else '' for x, y in zip(enroll, referral)}
    enroll_income = [0] * n

    for s, a in zip(seller, amount) :
        child, parent = s, enroll_parent[s]
        cur_income = a * 100
        while child :
            parent_income = cur_income // 10
            enroll_income[enroll_idx[child]] += cur_income - parent_income
            if parent_income == 0 :
                break
            cur_income = parent_income
            if parent == '' :
                break
            child, parent = parent, enroll_parent[parent]

    return enroll_income

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))
# [360, 958, 108, 0, 450, 18, 180, 1080]
print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["sam", "emily", "jaimie", "edward"], [2, 3, 5, 4]))
# [0, 110, 378, 180, 270, 450, 0, 0]