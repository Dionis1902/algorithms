def get_litres_dict(text):
    result_dict = {}

    for i in range((text_len := len(text)) - 2, -1, -1):
        if text[i] not in result_dict.keys():
            result_dict[text[i]] = text_len - i - 1

    if text[text_len - 1] not in result_dict.keys():
        result_dict[text[text_len - 1]] = text_len

    result_dict['*'] = text_len
    return result_dict


def boyer_moore(search_text, text):
    search_text_len = len(search_text)
    result_dict = get_litres_dict(search_text)
    if (text_len := len(text)) < search_text_len:
        return -1
    i = search_text_len - 1

    while i < text_len:
        k = 0
        is_break = False
        for j in range(search_text_len - 1, -1, -1):
            if text[i - k] != search_text[j]:
                if j == search_text_len - 1:
                    offset = result_dict[text[i]] if result_dict.get(text[i], False) else result_dict['*']
                else:
                    offset = result_dict[search_text[j]]
                i += offset
                is_break = True
                break
            k += 1
        if not is_break:
            return i - k + 1
    return -1


print(boyer_moore("world", "hello world!"))
