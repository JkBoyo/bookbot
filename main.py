import os
def main():
    file_contents = get_book(str(input()))
    get_word_count(file_contents)
    char_count = get_char_count(file_contents)
    print(char_count)
def get_book(book_name):
    books = os.listdir("./books/")
    book_fp = "./books/"
    for book in books:
        if book_name in book:
            book_fp += book
    with open(book_fp) as f:
        file_contents = f.read()
    return file_contents
def get_word_count(file):
    words = file.split()
    word_count = len(words)
    print(word_count)
def get_char_count(file):
    char_dict = {}
    lowered_file = file.lower()
    for char in lowered_file:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1    
    return char_dict

main()