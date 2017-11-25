from tkinter import*
import tkinter.messagebox

def gameWin() :
      tkinter.messagebox.showinfo("Win")
def gameDraw() :
      tkinter.messagebox.showinfo("Draw")
def checked(i) :
      global player
      global checkstate
      button = list[i]

      if button["text"] != "     " :
            return
      button["text"] = player
      button["bg"] = "yellow"
      
      if player == "X" :
            player = "O"
            button["bg"] = "yellow"
      else :
            player = "X"
            button["bg"] = "lightgreen"

      row = i // 3
      col = i % 3

      if list[row * 3]["text"] == list[row * 3 + 1]["text"] == list[row * 3 + 2]["text"] :
            gameWin()
      elif list[col]["text"] == list[col + 3]["text"] == list[col + 6]["text"] :
            gameWin()
      elif list[0]["text"] == list[4]["text"] == list[8]["text"] != "     " :
            gameWin()
      elif list[2]["text"] == list[4]["text"] == list[6]["text"] != "     " :
            gameWin()
      elif checkstate==8 :
            gameDraw()

      checkstate+=1

window = Tk()
player = "X"
list= []

for i in range(9) :
      b = Button(window, text="     ", command=lambda k=i: checked(k))
      b.grid(row=i//3, column=i%3)
      list.append(b)

checkstate=0

window.mainloop()

