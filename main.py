import sys
from stats import get_num_words, get_chars_dict, get_sorted_chars_list

def get_book_text(file_path):
  with open(file_path) as f:
    return f.read()

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  
  book_file_path = sys.argv[1]
  text = get_book_text(book_file_path)
  word_count = get_num_words(text)
  chars_dict = get_chars_dict(text)
  sorted_chars_list = get_sorted_chars_list(chars_dict)

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_file_path}...")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print("--------- Character Count -------")
  for char_dict in sorted_chars_list:
    if char_dict["char"].isalpha():
      print(f"{char_dict["char"]}: {char_dict["num"]}")
  print("============= END ===============")

main()
