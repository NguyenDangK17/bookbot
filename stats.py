def get_num_words(book_text):
    num_words = len(book_text.split())
    return num_words


def get_num_characters(book_text):
    num_characters = {}
    for char in book_text.lower():
        if char in num_characters:
            num_characters[char] += 1
        else:
            num_characters[char] = 1
    return num_characters


def sort_on(dict):
    return dict["num"]


def report_book(book_text):
    char_count = {}

    for char in book_text.lower():
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    result = [{"char": key, "num": value} for key, value in char_count.items()]
    result.sort(key=sort_on, reverse=True)
    return result
