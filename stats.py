def get_num_words(text):
  word_list = text.split()
  return len(word_list)


def get_chars_dict(text):
  char_count = {}
  lowercase_text = text.lower()
  for char in lowercase_text:
    if char in char_count:
      char_count[char] += 1
    else:
      char_count[char] = 1
  
  return char_count


def get_sorted_chars_list(chars_dict):

  list_of_char_dicts = []

  for char, num in chars_dict.items():
    individual_char_dict = {}
    individual_char_dict["char"] = char
    individual_char_dict["num"] = num
    list_of_char_dicts.append(individual_char_dict)

  def sort_on(dict):
    return dict["num"]
  
  list_of_char_dicts.sort(reverse=True, key=sort_on)

  return list_of_char_dicts