example_text = """Prepared do an dissuade be so whatever steepest. Yet her beyond looked either day wished nay. 
By doubtful disposed do juvenile an. Now curiosity you explained immediate why behaviour. An dispatched impossible of 
of melancholy favourable. Our quiet not heart along scale sense timed. Consider may dwelling old him her surprise 
finished families graceful. Gave led past poor met fine was new.
"""

# Split the example text based on dots => this should give us a list of
# sentences. For example, if the text was: "I like apples. He is tall." -
# after splitting it we would get a list of individual sentences: ["I like apples", "He is tall"]
sentences = example_text.split(".")

# Loop over sentences. This will take each sentence from the list and
# perform the following logic to it.
for sentence in sentences:
  # We split each sentence based on spaces => this gives us a list of all words in the sentence.
  words_in_sentence = sentence.split()
  # Next we calculate the number of words in the list.
  number_of_words_in_sentence = len(words_in_sentence)

  # Print a line before every sentence so we can see where one sentence starts and another finishes
  print("-" * 20)
  
  if number_of_words_in_sentence > 6:
    # Get a reversed version of the word list
    reversed_words = reversed(words_in_sentence)
    # Combine all words (that are now in reversed order) back into a sentence.
    # The following logic simply "joins" all words together by putting a space in between each word
    combined_sentence = " ".join(reversed_words)
    # Print the final reversed sentence
    print(combined_sentence)
  else:  # if the number number of words is not bigger than 6 => simply print out the default sentence without changing it 
    print(sentence)