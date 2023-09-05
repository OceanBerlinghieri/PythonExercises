def countLetters(text):
    return len(text.replace(" ", ""))

def countWords(text):
    words = text.split()
    return len(words)

def getText():
    return(input("Introduce your thoughts: "))

while True:
    if input("Introduce 0 if you want to exit: ") == '0':
        break
        
    text = getText()
    count = countLetters(text)
    words = countWords(text)

    print("You have shown your thoughts in",words , "words and", count, "letters")