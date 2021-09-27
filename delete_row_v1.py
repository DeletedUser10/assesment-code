from tkinter import *


root = Tk()
root.title('code')
root.geometry('800x510')

#Quits the program
def quit():
    root.destroy()



def frame_1():
    global entry_cus, entry_rec, entry_item, entry_num, framel
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
    framel2.grid(row= 2, column= 1, padx = 20, pady = 20, ipadx = 380, ipady= 100, sticky=N)


 
def append_list():
    #Global entries used 
    global customer_details, entry_num, entry_cus, entry_rec, entry_item, total_entries
    #Adds the user information to the list
    customer_details.append([entry_cus.get(), entry_rec.get(), entry_item.get(), entry_num.get()])
    # Deletes the text in the boxes 
    entry_cus.delete(0, END)
    entry_rec.delete(0,END)
    entry_item.delete(0,END)
    entry_num.delete(0,END)
    total_entries += 1
 

#buttons that excecute the program
def exceuite_buttons():
    append_b = Button(root, text = "Append details", command= append_list)
    append_b.place(x = 400, y = 473)
    print_b = Button(root, text = "Print details", command= print_details)
    print_b.place(x = 600, y = 473)


def delete():
    global e_del
    del_row = Label(root, text = "Row #").grid(row = 3, column= 1, sticky= W )
    e_del = Entry(root)
    e_del.place(x = 54, y = 475)
    del_button = Button(root, text = "Delete row", command = delete_button)
    del_button.place(x = 180, y= 473)

def delete_button():
    global customer_details, e_del, total_entries, name_count, framel2

    del customer_details[int(e_del.get())]
    total_entries = total_entries -1
    e_del.delete(0 ,END)


#Ghost labels that cover labels as they are deleted
    Label(framel2, text="                          ", bg = "white").grid(column=0,row=name_count+7) 
    Label(framel2, text="                          ", bg = 'white').grid(column=1,row=name_count+7)
    Label(framel2, text="                          ", bg = "white").grid(column=4,row=name_count+7)
    Label(framel2, text="                          ", bg = "white").grid(column=6,row=name_count+7)
    Label(framel2, text="                          ", bg = "white").grid(column=8,row=name_count+7)



    print_details()
  
    quit_b.grid(row = 0, column= 0 )
    framel.grid(row= 1, column=0)
    framel2.grid(row= 2, column= 0 )
    framel2.grid(row= 2, column= 0, padx = 20, pady = 20, ipadx = 60, ipady= 100, sticky=N)

def quit_button():
    global quit_b
    quit_b = Button(root, text = "quit" , command = quit, padx = 30)
    quit_b.grid(column=1, row= 0, sticky= W ) 


def print_details():
    global total_entries, name_count, framel2, framel, quit_b
    name_count = 0
    #creating column headings
    Label(framel2, text = "Row", bg = "white").grid(row=0, column=0)
    Label(framel2, text = "Name", bg = "white").grid(row=0, column=1)
    Label(framel2, text = "Reciept Number", bg = "white").grid(row=0, column=4)
    Label(framel2, text = "Item Hired", bg = "white").grid(row=0, column=6)
    Label(framel2, text = "Number Hired", bg = "white").grid(row=0, column=8)
#loops through the list
    while name_count < total_entries: 
        Label(framel2, text=name_count, bg = 'white').grid(column=0,row=name_count+8)  
        Label(framel2, bg = 'white', text=(customer_details[name_count][0])).grid(column=1,row=name_count+8)
        Label(framel2, bg = 'white', text=(customer_details[name_count][1])).grid(column=4,row=name_count+8)
        Label(framel2, bg = 'white',text=(customer_details[name_count][2])).grid(column=6,row=name_count+8)
        Label(framel2, bg = 'white', text=(customer_details[name_count][3])).grid(column=8,row=name_count+8) 
        
        name_count +=  1

    ghost_label3 = Label(framel2, text = "                    " , bg = 'white').grid(row=0, column= 3 )
    ghost_label4 = Label(framel2, text = "                    " , bg = 'white').grid(row=0, column= 5 )
    ghost_label5 = Label(framel2, text = "                    " , bg = 'white').grid(row=0, column= 7 )

  
  
  
    quit_b.grid(row = 0, column= 0 )
    framel.grid(row= 1, column=0)
    framel2.grid(row= 2, column= 0 )
    framel2.grid(row= 2, column= 0, padx = 20, pady = 20, ipadx = 100, ipady= 150, sticky=N)
    framel.grid(padx = 20, pady = 20, ipadx = 35, ipady= 30)



def main():
    global root, customer_details, total_entries
    quit_button()
    total_entries = 0
    customer_details = []
    frame_1()
    frame_2()
    delete()
    exceuite_buttons()
    root.mainloop()


main()
