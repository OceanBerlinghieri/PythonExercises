#IMPORTS
import random
#FUNCTIONS
def selectText(texts):
    return texts[random.randint(0, len(texts) - 1)]

def fillWords(wordMap):
    wordMap["noun"] = input("Introduce a noun: ")
    wordMap["adjective"] = input("Introduce an adjective: ")
    wordMap["color"] = input("Introduce a color: ")
    wordMap["person"] = input("Introduce a person: ")

#INIT
wordMap = {}

while True:
    option = input("Introduce 0 if you want to exit: ")
    
    if option == '0':
        break
    
    fillWords(wordMap)

    TEXTS = ["THE " + wordMap["color"] + wordMap["noun"] + " was running against " + wordMap["person"],
            "I am "+wordMap["noun"],
            "Your " + wordMap["noun"] + " is very " + wordMap["adjective"]]

    selectedText = selectText(TEXTS)
    print(selectedText.upper())
    
    print("Do you want to exit?")
