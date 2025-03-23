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
