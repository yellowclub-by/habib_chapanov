import random
from tkinter import*
root = Tk()

root.title("Камень, ножницы, бумага")
root.geometry("600x400")
root.resizable(width = False , height = False)

use_text=Label(root,text="player",font=20,bg="white")
use_text.place(x=50,y=50)
c_t=Label(root,text="comp",font=20,bg="green")
c_t.place(x=50,y=75)
c_c=Label(root,text="comp took",font=20,bg="yellow")
c_c.place(x=50,y=100)
win=Label(root,text="winner",font=20,bg="purple")
win.place(x=50,y=125)

def action(btn):
    lst=["камень","ножницы","бумага"]
    computer=random.choice(lst)
    user=btn['text']
    print(computer,user)

stone = Button(root, text="stone", bg="green")
stone.place(x=50, y=10, width=50, height=20)
stone.config(command=lambda:action(stone))

paper = Button(root, text="paper", bg="yellow")
paper.place(x=100, y=10, width=50, height=20)
paper.config(command=lambda:action(paper))

scissor = Button(root, text="scissor", bg="purple")
scissor.place(x=150, y=10, width=50, height=20)
scissor.config(command=lambda:action(scissor))

root.mainloop()
