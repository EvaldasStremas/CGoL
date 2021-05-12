# Print a version of the paragraph in which the first and every other letter from every word is capitalized. (Example: The quick brown fox -> ThE QuIcK BrOwN FoX)

example_text = "The quick brown fox fox fox fox"
words = example_text.split()

# Converting each words in upper case as text example
def word_convert(example_text):
    string_list = list(example_text)
    text_len = len(example_text)

    i = 0
    while i < text_len: 
        if i % 2 != 1:
            string_list[i] = string_list[i].upper()
        i += 1
    new_string = "".join(string_list)
    return new_string

new_text = []

for word in words:
    new_text.append((word_convert(word)))
    new_string = " ".join(new_text)
    
print(new_string)