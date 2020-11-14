import random

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


def PlaceWords():
    for word in words:
        if len(word) > rowMax or len(word) > colMax : continue
        direction = random.randint(0,3)
        if direction == 0:
            print("placing",word,"from left to right")
            min = 0
            max = colMax - len(word)
        elif direction == 1:
            print("placing",word,"from right to left")
            min = len(word) - 1
            max = colMax - 1
        elif direction == 2:
            print("placing",word,"from toop to bottom")
            min = 0
            max = rowMax - len(word)
        elif direction == 3:
            print("placing",word,"from bottom to top")
            min = len(word) - 1
            max = rowMax - 1
        print("Word length is ",len(word),"so: ")
        print("min: ",min,"max: ",max)
        square = random.randint(min,max)
        print("Square chosen is ",square)
        if direction < 2:
            row = random.randint(0,rowMax-1)
            col = square
            print(" in row ",row)
        else:
            col = random.randint(0,colMax-1)
            row = square
            print(" in column ", col)

PlaceWords()


















