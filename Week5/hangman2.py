import random

theWords = []
file = open("EnglishWords.txt", "r")
for line in file:
    line = line.rstrip()
    theWords.append(line)
word = random.choice(theWords)
count = 0
win = False
guesses = ""
answer = ""
for i in range(len(word)): answer += "_"
while (count < 10 and win is False):
    count = count + 1
    guess = input("Enter guess: ")
    guesses = guesses + guess
    tmp = ""
    i = 0
    while i < len(word):
        if (word[i] == guess):
            tmp = tmp + guess
        else:
            tmp = tmp + answer[i]
        i = i + 1
    if (answer != tmp):
        print("good guess")
        count = count - 1
        answer = tmp
    else:
        print("not a good guess")
    if (answer == word):
        print("Well done you win !")
        win = True
    print(str(10 - count) + "/10 guesses left.")
    print("your guesses: " + guesses)
    print("The word so far: " + answer)


    
