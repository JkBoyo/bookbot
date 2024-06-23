import os
def main():
    print("Enter the whole or partial name of a book that has been added to the /books directory to generate a report.")
    book_name = str(input())
    os.system('cls' if os.name=='nt' else 'clear')
    file_contents = get_book(book_name)
    word_count = get_word_count(file_contents)
    char_list = get_char_count(file_contents)
    write_report_func(book_name, word_count, char_list)
def get_book(book_name):
    books = os.listdir("./books/")
    book_fp = "./books/"
    for book in books: #loop for doing a substring in string search.
        if book_name.lower() in book.lower():
            book_fp += book
            break #don't wanna deal with potential multiple files having matching parts. Ensures only one path returned.
    with open(book_fp) as f: #getting file contents
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
    for char in lowered_file: #generating character count dict
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1    
    for key, val in char_dict.items(): #making a list from my dict for sorting purposes
        if(key.isalpha()): #eliminating symbols
            char_list.append([key, val])
    char_list.sort(reverse=True, key= lambda x: x[1]) #sorting said list.
    return char_list
def write_report_func(book_name, word_count, char_list):
    print(f"--- Begin report of {book_name} ---")
    print(f"{word_count} words found in the document\n")
    for char in char_list:
        print(f"the {char[0]} character was found {char[1]} times")
    print(f"--- End report ---")
main()