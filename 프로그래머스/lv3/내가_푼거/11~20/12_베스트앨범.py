from collections import defaultdict

def solution(genres, plays):
    music_dict = {}
    genre_dict = defaultdict(int)

    for i, info in enumerate(zip(genres, plays)) :
        genre, play = info
        music_dict[i] = {'genre' : genre, 'play' : play}
        genre_dict[genre] += play

    sorted_genre = sorted(genre_dict.items(), key = lambda x : x[1], reverse = True)

    answer = []

    for genre, _ in sorted_genre :
        sorted_music = sorted(music_dict.items(), key = lambda x : -x[1]['play'])
        answer += [x[0] for x in sorted_music if x[1]['genre'] == genre][:2]

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))