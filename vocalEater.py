import time

word = input("Introduce una palabra: ")

word = word.upper()

word_without_vowels = ""
for letter in word:
    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        continue

    word_without_vowels += letter

print(word_without_vowels)

time.sleep(3)
