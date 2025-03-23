def count_words(text):
    words = text.split()
    return len(words)


def count_chars(text):
    text_lower = text.lower()
    char_count = {}

    for char in text_lower:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


def sort_on(dict):
    return dict["count"]


def sort_list_dicts(dict_chars):
    sorted_list = []

    for key in dict_chars:
        new_dict = {"char": key, "count": dict_chars[key]}
        sorted_list.append(new_dict)

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list
