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
     
    entry_cus= Entry(framel)
    entry_cus.grid(row= 2, column= 1, ipadx = 30)
    entry_rec = Entry(framel)
    entry_rec.grid(row=2, column=7, sticky= E)
     #general information Labels
    general = Label(framel, text = "General Information").grid(column=0, row = 0)
    
    #Glost Labels
    ghost_label1 = Label(framel, text = "    " ).grid(row=1, column= 0 )
    ghost_label3 = Label(framel, text = "    " ).grid(row=2, column= 2 )
    ghost_label4 = Label(framel, text = "    " ).grid(row=2, column= 3 )
    ghost_label5 = Label(framel, text = "    " ).grid(row=2, column= 4 )
    
    customer_name = Label(framel, text = "Customer Name").grid(column= 0, row= 2)
    r_label = Label(framel, text = "Reciept Number ").grid(row = 2, column=6)
    Label(framel, text="").grid(row = 3, column=0)

def quit_button():
    quit_b = Button(root, text = "quit" , command = quit, padx = 30)
    quit_b.grid(column=1, row= 0, sticky= W ) 


def main():
    quit_button()
    frame_1()
    root.mainloop()


main()