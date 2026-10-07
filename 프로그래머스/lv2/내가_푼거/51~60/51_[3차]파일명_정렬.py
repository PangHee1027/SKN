def solution(files):
    file_dict_list = []
    for file in files :
        file_dict = {}
        num_idx = []
        for i in range(len(file)) :
            if file[i].isdecimal() :
                num_idx.append(i)
            if num_idx and (not file[i].isdecimal() or len(num_idx) == 5) :
                break
        file_dict["head"], file_dict["number"], file_dict["tail"], file_dict["original"] = file[:num_idx[0]], file[num_idx[0] : num_idx[-1] + 1], file[num_idx[-1] + 1 :], file
        file_dict_list.append(file_dict)

    file_dict_list.sort(key = lambda x : int(x["number"])) 
    file_dict_list.sort(key = lambda x : x["head"].lower()) 

    answer = [x["original"] for x in file_dict_list]
    return answer

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
# print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))