def solution(word):
    alph_dict = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    weights = [781, 156, 31, 6, 1]  # 딕셔너리 대신 리스트 활용
    
    return sum(weights[i] * alph_dict[c] + 1 for i, c in enumerate(word))