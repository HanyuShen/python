from tkinter import Tk,PhotoImage,Button,messagebox

def create_buttons():
    square[0] = Button(window,image=available_space,width="100",
                       height="100",command=lambda: handle_button_click(0))

    square[0].place(x=0,y=0)

    square[1] = Button(window,image=player1_taken,width="100",
                       height="100",command=lambda: handle_button_click(1))

    square[1].place(x=100,y=100)

    square[2] = Button(window,image=player2_taken,width="100",
                       height="100",command=lambda: handle_button_click(2))

    square[2].place(x=200,y=200)

counter = 0

def square_taken():
    messagebox.showinfo("Square Taken","Square already taken choose another!")

def handle_button_click(button_number):
    print("Button ",button_number, "was clicked")
    global counter
    if counter % 2 == 0:
        square[button_number].configure(image=player1_taken,command=square_taken)
    else:
        square[button_number].configure(image=player2_taken,command=square_taken)

counter += 1


 
window = Tk()
window.title("OXO Game")
window.geometry("300x300")



available_space = PhotoImage(file="myButton.png")
player1_taken = PhotoImage(file="myButtonP1.png")
player2_taken = PhotoImage(file="myButtonP2.png")
winner = PhotoImage(file="winner.png")



square = [None]*9
create_buttons()


window.mainloop()
