from tkinter import Tk,Canvas
import random

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

snake=[]
snakeSize = 15
snake.append(canvas.create_rectangle(snakeSize,snakeSize,snakeSize*2,snakeSize*2,fill="white"))

score = 0
txt = "Score: " + str(score)
scoreText = canvas.create_text(width/2,10,fill="white",font="Times 20 italic bold",text=txt)

window.mainloop()
    
