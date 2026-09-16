def solution(data, ext, val_ext, sort_by):
    data_list = []
    answer = [[]]

    for a, b, c, d in data :
        match ext :
            case "code" :
                if a < val_ext :
                    data_list.append([a, b, c, d])
            case "date" :
                if b < val_ext :
                    data_list.append([a, b, c, d])
            case "maximum" :
                if c < val_ext :
                    data_list.append([a, b, c, d])
            case "remain" :
                if d < val_ext :
                    data_list.append([a, b, c, d])
    match sort_by :
        case "code" :
            data_list.sort(key=lambda x: x[0])
        case "date" :
            data_list.sort(key=lambda x: x[1])
        case "maximum" :
            data_list.sort(key=lambda x: x[2])
        case "remain" :
            data_list.sort(key=lambda x: x[3])
    return data_list

solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]],
         "date", 20300501, "remain")