from tkinter import *


root = Tk()
root.title('code')

#Quits the program
def quit():
    root.destroy()



def frame_1():
    global entry_cus, entry_rec, entry_item, entry_num
    framel = Frame(root, highlightbackground= 'grey', highlightthickness= 1)
    framel.grid(row= 1, column= 1, padx = 20, pady = 20, ipadx = 40, ipady= 30)
    
    #Entries in frame 1
    entry_cus= Entry(framel)
    entry_cus.grid(row= 2, column= 1, ipadx = 30)
    entry_rec = Entry(framel)
    entry_rec.grid(row=2, column=7, sticky= E)
    entry_item = Entry(framel)
    entry_item.grid(row = 4, column= 1, ipadx=30)
    entry_num = Entry(framel)
    entry_num.grid(row = 4, column = 7)
     #general information Labels
    general = Label(framel, text = "General Information").grid(column=0, row = 0)
    
    #Glost Labels 
    ghost_label1 = Label(framel, text = "    " ).grid(row=1, column= 0 )
    ghost_label3 = Label(framel, text = "    " ).grid(row=2, column= 2 )
    ghost_label4 = Label(framel, text = "    " ).grid(row=2, column= 3 )
    ghost_label5 = Label(framel, text = "    " ).grid(row=2, column= 4 )
    
    #Labels that are within frame 1
    customer_name = Label(framel, text = "Customer Name").grid(column= 0, row= 2)
    r_label = Label(framel, text = "Reciept Number ").grid(row = 2, column=6)
    Label(framel, text="").grid(row = 3, column=0)
    i_label = Label(framel, text = "Item hired").grid(row = 4, column= 0)
    n_label = Label(framel, text= "Number hired").grid(row = 4, column= 6)

#Second frame created where the list will be printed to
def frame_2():
    global framel2
    framel2 = Frame(root, highlightbackground= 'grey', highlightthickness= 1, bg = 'white')
    framel2.grid(row= 2, column= 1, padx = 20, pady = 20, ipadx = 325, ipady= 100, sticky=N)

def delete_button():
    return
 
def append_list():
     return



def exceuite_buttons():
    append_b = Button(root, text = "Append details", command= append_list)
    append_b.place(x = 400, y = 473)
    print_b = Button(root, text = "Print details", command= print_details)
    print_b.place(x = 600, y = 473)


def delete():
    del_row = Label(root, text = "Row #").grid(row = 3, column= 1, sticky= W )
    e_del = Entry(root)
    e_del.place(x = 54, y = 475)
    del_button = Button(root, text = "Delete row", command = delete_button)
    del_button.place(x = 180, y= 473)



def quit_button():
    quit_b = Button(root, text = "quit" , command = quit, padx = 30)
    quit_b.grid(column=1, row= 0, sticky= W ) 


def print_details():
    return



def main():
    quit_button()
    cutomer_details = []
    frame_1()
    frame_2()
    delete()
    exceuite_buttons()
    root.mainloop()


main()