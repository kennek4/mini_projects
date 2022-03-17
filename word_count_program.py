import time

file = "Mini Projects/mini projects/word_count_test_file.txt"
hnd = open(file)

wordFrequency = {}

# for line in hnd:
#     words = line.split()
#     for word in words:
#         wordFrequency[word] = wordFrequency.get(word, 0) + 1

# mostWord = None
# mostCount = None
# for word, count in wordFrequency.items():
#     if mostCount is None or count > mostCount:
#         mostCount = count
#         mostWord = word

# # print(wordFrequency)

# print(mostWord, mostCount)

start = time.time()

for line in hnd:
    words = line.split()

    for word in words:

        word = word.casefold()

        if word in wordFrequency:
            print("\nNOT NEW")
            wordFrequency[word] = wordFrequency.get(word, 0) + 1
            print(word)
            print("Count: " + str(wordFrequency.get(word, 0)))

        elif word not in wordFrequency:
            print("\nNEW")
            wordFrequency[word] = wordFrequency.get(word, 0) + 1
            print(word)
            print("Count: " + str(wordFrequency.get(word, 0)))

end = time.time()

print(end-start)

total_words = sum(wordFrequency.values())

print("Total Words: " + str(total_words))
