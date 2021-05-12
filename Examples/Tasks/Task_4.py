# Print a version of the paragraph in which all words are in reversed order. (Example: The quick brown fox -> fox brown quick The)

example_text = "The quick brown fox"

words = example_text.split()
reversed_list = words[::-1]

for word in reversed_list:
    new_string = " ".join(reversed_list)

print(new_string)