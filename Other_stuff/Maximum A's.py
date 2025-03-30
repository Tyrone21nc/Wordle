"""
Write code that prints out the word with the maximum number of a's in a given set of words by the user
"""

word = input("Enter a word (quit to stop): ").lower()
all_words = []
while word != "quit":
    all_words.append(word)
    word = input("Enter a word (quit to stop): ").lower()

the_As = 0
num_of_A = []
for i in range(len(all_words)):
    for j in range(len(all_words[i])-1):
        the_word = all_words[i]
        if "a" == the_word[j:j + 1]:
            the_As += 1
    num_of_A.append(the_As)

print()
for i in range(len(num_of_A) - 1):
    big = num_of_A[i]
    if big < num_of_A[i + 1]:
        big = num_of_A[i + 1]
print(big)
