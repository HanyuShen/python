
word1 = "happy"
word2 = "sunny"
word3 = "funny"
word4 = "honey"

def GenerateGrid():
    grid = [['-' for x in range(colMax)] for y in range(rowMax)]
    return grid

def GetWords():
    theWords = ["happy","cheerful","chipper","effervescent","jaunty","jolly"]
    return theWords

def GetWordsFromUser():
    theWords = []
    while True:
        word = input("Enter a word and press <enter> (or just press <enter> to finish): ")
        if word != "": theWords.append(word)
        else:return theWords
     
words = GetWords()

def DisplayWords():
    for word in words:
        print(word)

DisplayWords()

def DisplayGrid():
    for row in range(rowMax):
        for col in range(colMax):
            print(grid[row][col] + ' ',end="")
        print()


rowMax = int(input("Enter number of rows: "))
colMax = int(input("Enter number of columns: "))
grid = GenerateGrid()
DisplayGrid()

