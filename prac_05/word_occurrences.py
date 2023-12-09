text = input("Text: ")
word_occurrences = text.split()
words = {}
for word in word_occurrences:
    word_count = words.get(word, 0)  # get value of a key
    words[word] = word_count + 1

words_to_print = list(words)
words_to_print.sort()
for word in words_to_print:
    print(f"{word} : {words[word]}")
