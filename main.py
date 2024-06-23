import os
def main():
    print("Enter a whole name or part of a name that has been moved to the /books directory.")
    book_name = str(input())
    os.system('cls' if os.name=='nt' else 'clear')
    file_contents = get_book(book_name)
    word_count = get_word_count(file_contents)
    char_list = get_char_count(file_contents)
    write_report_func(book_name, word_count, char_list)
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
    return word_count
def get_char_count(file):
    char_dict = {}
    lowered_file = file.lower()
    char_list = []
    for char in lowered_file:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1    
    for key, val in char_dict.items():
        if(key.isalpha()):
            char_list.append([key, val])
    char_list.sort(reverse=True, key= lambda x: x[1])
    return char_list
def write_report_func(book_name, word_count, char_list):
    print(f"--- Begin report of {book_name} ---")
    print(f"{word_count} words found in the document\n")
    for char in char_list:
        print(f"the {char[0]} character was found {char[1]} times")
    print(f"--- End report ---")
main()