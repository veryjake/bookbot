from stats import word_count, each_character, sort_dict
import sys

def main():

  if len(sys.argv) < 2: 
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  book_path = sys.argv[1]
  text = get_book_text(book_path)
  result = word_count(text)
  result2 = each_character(text)
  result3 = sort_dict(result2)

  print(f"============ BOOKBOT ============\n"
        f"Analyzing book found at {book_path}...\n"
        "----------- Word Count ----------\n"
        f"Found {result} total words\n"
        "--------- Character Count -------")
  for key, value in result3.items():
    if key.isalpha():
      print(key + ':', value)
  print("============= END ===============")

def get_book_text(path):
  with open(path) as f:
    return f.read()
  

main()