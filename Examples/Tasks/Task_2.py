# Find the shortest sentence from the paragraph. Print the sentence and the number of words in that sentence.

example_text = """Prepared do an dissuade be so whatever steepest. Yet her beyond looked either day wished nay. 
By doubtful disposed do juvenile an. Now curiosity you explained immediate why behaviour. An dispatched impossible of 
of melancholy favourable. Our quiet not heart along scale sense timed. Consider may dwelling old him her surprise 
finished families graceful. Gave led past poor met fine was new.
"""

# Count words in each sentence and store in list of lists
def sentence_count(str):
    sentences = example_text.split(". ")
    listoflists = []
    
    for sentence in sentences:
        words = sentence.split()
        sublist = []
        words_len = len(words)
        sublist.append(sentence)
        sublist.append(words_len)
        listoflists.append(sublist)
    return listoflists

# print(sentence_count(example_text))

# Bubble sort algorithm in sublist
def Sort(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (sub_li[j][1] > sub_li[j + 1][1]):
                tempo = sub_li[j]
                sub_li[j]= sub_li[j + 1]
                sub_li[j + 1]= tempo
    return sub_li

sub_li = sentence_count(example_text)

# print(Sort(sub_li)[0])

sorted_text = Sort(sub_li)[0][0]

sorted_text_without_n = sorted_text.replace('\n','')

print('Shortest sentece is this: ', sorted_text_without_n)
print('Words in shortest sentence is: ', Sort(sub_li)[0][1])