# Find the number of times each word in the paragraph is used. Print the top 3 most used words.

example_text = """Prepared do an dissuade be so whatever steepest. Yet her beyond looked either day wished nay. 
By doubtful disposed do juvenile an. Now curiosity you explained immediate why behaviour. An dispatched impossible of 
of melancholy favourable. Our quiet not heart along scale sense timed. Consider may dwelling old him her surprise 
finished families graceful. Gave led past poor met fine was new.
"""

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        word_without_dot = word.replace('.','')
        if word_without_dot in counts:
            counts[word_without_dot] += 1
        else:
            counts[word_without_dot] = 1
    return counts

wordsFreqDict = word_count(example_text)

# print(word_count(example_text))

listofTuples = sorted(wordsFreqDict.items() , reverse=True, key=lambda x: x[1])

# print(word_count(example_text))

for x in range(3):
  print(listofTuples[x])