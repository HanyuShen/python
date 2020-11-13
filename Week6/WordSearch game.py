
word1 = "happy"
word2 = "sunny"
word3 = "funny"
word4 = "honey"

def GenerateGrid():
    grid = [['-' for x in range(colMax)] for y in range(rowMax)]
    return grid


def DisplayGrid():
    for row in range(rowMax):
        for col in range(colMax):
            print(grid[row][col] + ' ', end="")
        print()
def GetWords():
    theWords = ["happy","cheerful","chipper","effervescent","jaunty","jolly"]
    return theWords

def GetWords():
    theWords = []
    while True:
        word = input("Enter a word and press <enter> (or just press <enter> to finish) :")
        if word != "": theWords.append(word)
        else:return theWords

def DisplayWords():
    for word in words:
        print(word)

words = GetWords()
words = DisplayWords()



rowMax = int(input("Enter number of rows: "))
colMax = int(input("Enter number of columns: "))
grid = GenerateGrid()
DisplayGrid()
