from tkinter import Tk,PhotoImage,Button

def create_buttons():
    square[0] = Button(window,image=available_space,width="100",
                       height="100",command=None)

    square[0].place(x=0,y=0)
def create_buttons2():
    square[2] = Button(window,image=player1_taken,width="100",
                       height="100",command=None)

    square[2].place(x=100,y=100)
def create_buttons3():
    square[4] = Button(window,image=player2_taken,width="100",
                       height="100",command=None)

    square[4].place(x=200,y=200)
    
    
window = Tk()
window.title("OXO Game")
window.geometry("300x300")



available_space = PhotoImage(file="myButton.png")
player1_taken = PhotoImage(file="myButtonP1.png")
player2_taken = PhotoImage(file="myButtonP2.png")
winner = PhotoImage(file="winner.png")



square = [None]*9
create_buttons()
create_buttons2()
create_buttons3()

window.mainloop()
