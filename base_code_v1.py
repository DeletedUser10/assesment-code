from tkinter import *


root = Tk()
root.title('code')
root.geometry("800x400")

#Quits the program
def quit():
    root.destroy()

def print_details():
    return


def frame_1():
    global entry_cus, entry_rec, entry_item, entry_num
    framel = Frame(root, highlightbackground= 'grey', highlightthickness= 1)
    framel.grid(row= 1, column= 1, padx = 20, pady = 20, ipadx = 40, ipady= 30)

def quit_button():
    quit_b = Button(root, text = "quit" , command = quit, padx = 30)
    quit_b.grid(column=1, row= 0, sticky= W ) 


def main():
    quit_button()
    frame_1()
    root.mainloop()


main()