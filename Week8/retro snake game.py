from tkinter import Tk,Canvas
import random


def placeFood():
    global food,foodX,foodY
    food = canvas.create_rectangle(0,0,snakeSize,snakeSize,fill="steel blue")
    foodX = random.randint(0,width-snakeSize)
    foodY = random.randint(0,height-snakeSize)
    canvas.move(food,foodX,foodY)
def leftKey(event):
    global direction
    direction = "left"
    
def rightKey(event):
    global direction
    direction = "right"

def upKey(event):
    global direction
    direction = "up"

def downKey(event):
    global direction
    direction = "down"

def setWindowDimensions(w,h):
    window = Tk()
    window.title("Snake Game")
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry("%dx%d+%d+%d" % (w,h,x,y))
    return window


width = 550
height = 550


window = setWindowDimensions(width,height)
canvas = Canvas(window,bg="black",width=width,height=height)

canvas.bind("<Left>", leftKey)
canvas.bind("<Right>", rightKey)
canvas.bind("<Up>", upKey)
canvas.bind("<Down>", downKey)
canvas.focus_set()

direction  = "right"

snake=[]
snakeSize = 15
snake.append(canvas.create_rectangle(snakeSize,snakeSize,snakeSize*2,snakeSize*2,fill="white"))


score = 0
txt = "Score: " + str(score)
scoreText = canvas.create_text(width/2,10,fill="white",font="Times 20 italic bold",text=txt)

placeFood()

window.mainloop()
    
