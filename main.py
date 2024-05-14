def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = get_num_letters(text)
    print('--- Begin report of books/frankenstein.txt ---')
    print(f"{num_words} words found in the document")
    # print(f"each letter was found: {letter_count}")
    letter_list = list(letter_count)
    letter_list.sort()
    print(letter_list)

    print('--- End report ---')


def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letters(text):
    lower_case = text.lower()
    letter_count = {
        "a": lower_case.count('a'),
        "b": lower_case.count('b'),
        "c": lower_case.count('c'),
        "d": lower_case.count('d'),
        "e": lower_case.count('e'),
        "f": lower_case.count('f'),
        "g": lower_case.count('g'),
        "h": lower_case.count('h'),
        "i": lower_case.count('i'),
        "j": lower_case.count('j'),
        "k": lower_case.count('k'),
        "l": lower_case.count('l'),
        "m": lower_case.count('m'),
        "n": lower_case.count('n'),
        "o": lower_case.count('o'),
        "p": lower_case.count('p'),
        "q": lower_case.count('q'),
        "r": lower_case.count('r'),
        "s": lower_case.count('s'),
        "t": lower_case.count('t'),
        "u": lower_case.count('u'),
        "v": lower_case.count('v'),
        "w": lower_case.count('w'),
        "x": lower_case.count('x'),
        "y": lower_case.count('y'),
        "z": lower_case.count('z')
    }
    return letter_count

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()