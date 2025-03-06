def word_count(text):
  result = len(text.split())
  return result

def each_character(text):
  d = {}
  lowered_text = text.lower()
  words = list(lowered_text)

  for letter in words:
    if letter in d.keys():
      d[letter] += 1
    else:
      d[letter] = 1
  return d

def sort_dict(book):
  sorted_dict = dict(sorted(book.items(), key=lambda x: x[1], reverse=True))
  return sorted_dict