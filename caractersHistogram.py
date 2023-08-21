"""Program to count letters in a line
If character found on file is space or line break, we should
not include it on the dictionary
Converts the items in the dictionaryt to a sorted list
and finally writes the result on a new file"""

if __name__ == "__main__":
    counts = {}
    f = input("Introduce name of file: ")
    
    stream = open(f, "rt", encoding="utf-8")
    line = stream.readline().lower()
    
    while line != '':
        for char in line:
            if char == '\n' or char == ' ':
                break
            if char not in counts:
                counts[char] = 1
            else: 
                counts[char] = counts[char] + 1
        line = stream.readline()
    stream.close()
    
    stream = open(f + '.hist', 'w')
    ordered = sorted(list(counts.items()))
    for elem in ordered:
        stream.write(str(elem[0]) + '->' + str(elem[1]) + '\n')

