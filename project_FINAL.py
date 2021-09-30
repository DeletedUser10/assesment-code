from tkinter import *
from tkinter import messagebox


root = Tk()
root.title('Item hire program')

#Quits the program
def quit():
    root.destroy()


#Function that prints details onto the screen
def print_details():
    #global varriables used 
    global total_entries, name_count, framel2, framel, quit_b
    name_count = 0
    #creating column headings
    Label(framel2, font=("Helvetica 10 bold"), text = "Row", bg = "white").grid(row=0, column=0)
    Label(framel2, font=("Helvetica 10 bold"), text = "Name", bg = "white").grid(row=0, column=2)
    Label(framel2, font=("Helvetica 10 bold"), text = "Reciept Number", bg = "white").grid(row=0, column=4)
    Label(framel2, font=("Helvetica 10 bold"), text = "Item Hired", bg = "white").grid(row=0, column=6)
    Label(framel2, font=("Helvetica 10 bold"), text = "Number Hired", bg = "white").grid(row=0, column=8)
#loops through the list
    while name_count < total_entries: 
        Label(framel2, text=name_count, bg = 'white').grid(column=0,row=name_count+8)  
        Label(framel2, bg = 'white', text=(customer_details[name_count][0])).grid(column=2,row=name_count+8)
        Label(framel2, bg = 'white', text=(customer_details[name_count][1])).grid(column=4,row=name_count+8)
        Label(framel2, bg = 'white',text=(customer_details[name_count][2])).grid(column=6,row=name_count+8)
        Label(framel2, bg = 'white', text=(customer_details[name_count][3])).grid(column=8,row=name_count+8) 
        
        name_count +=  1
    #ghost labels 
    ghost_label3 = Label(framel2, text = "                    " , bg = 'white').grid(row=0, column= 3 )
    ghost_label9 = Label(framel2, text = "                    " , bg = 'white').grid(row=0, column= 1 )
    ghost_label4 = Label(framel2, text = "                    " , bg = 'white').grid(row=0, column= 5 )
    ghost_label5 = Label(framel2, text = "                    " , bg = 'white').grid(row=0, column= 7 )
  
    quit_b.grid(row = 0, column= 0 )
    framel.grid(row= 1, column=0)
    framel2.grid(row= 2, column= 0 )
    framel2.grid(row= 2, column= 0, padx = 20, pady = 20, ipadx = 100, ipady= 100, sticky=N)
    framel.grid(padx = 20, pady = 20, ipadx = 35, ipady= 30)
    framel3.grid(row= 3, column= 0, padx = 20, pady = 10, ipadx = 80, ipady= 5, sticky= N)

#general error check
def input_check():
    #global varriables used 
    global framel, entry_num, entry_rec, entry_cus, entry_item, total_entries
    #error checke varriable
    error_check = 0  
    #if nothing is entered in customer entry      
    if len(entry_cus.get()) == 0:
        #error message box will be displayed
        messagebox.showerror("Customer name", "Customer name is required")
        #error check will equal 1
        error_check = 1
    #if nothing is entered in item entry
    if len(entry_item.get()) == 0:
        #error message box will be displayed
        messagebox.showerror("Item Hired", "Item name is required")
        #error check will equal 1
        error_check = 1
    #if nothing is entered in reciept entry
    if len(entry_rec.get()) == 0:
        #error message box will be displayed
        messagebox.showerror("Reciept Number", "Reciept Number is required")
        #error check will equal 1
        error_check = 1

    #try and except function used to make sure only integers are entered
    try:# if nothing is inputed into number entry
        if len(entry_num.get()) == 0:
            #error message box will be displayed
            messagebox.showerror("Number Hired", "entry number is required")
            #error check will equal 1
            error_check = 1

        if (entry_num.get().isdigit):
            #if integer entered is more than 500 or less than 
            if int(entry_num.get()) == 0 or int(entry_num.get()) > 500:
                #error message box will be displayed
                messagebox.showerror("Number Hired", "Number hired must be between 1 and 500")
                #error check will equal 1
                error_check = 1

    except: #error message box will be displayed
            messagebox.showerror("Number Hired", "please enter a number")
            #error check will equal 1
            error_check = 1
    
    #if error check is 0
    if error_check == 0 : 
        #append list function will be excecuted
        append_list()

#first frame function
def frame_1():
    #global varriables used 
    global entry_cus, entry_rec, entry_item, entry_num, framel
    #frame 1 creation
    framel = Frame(root, highlightbackground= 'grey', highlightthickness= 1)
    #frame 1 grid
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
    
    #Ghost Labels 
    ghost_label1 = Label(framel, text = "    " ).grid(row=1, column= 0 )
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
    #frame 2 position
    framel2.grid(row= 2, column= 1, padx = 20, pady = 20, ipadx = 380, ipady= 100, sticky=N)


#third frame
def frame3():
    #global varriables used
    global framel3, e_del
    #frame 3 creation
    framel3 = Frame(root, highlightbackground= 'grey', highlightthickness= 1)
    #frame 3 placement
    framel3.grid(row= 3, column= 1, padx = 20, pady = 10, ipadx = 80, ipady= 5, sticky= N)

    # delete excecute buttons within frame 3
    del_row = Label(framel3, text = "Row Number")
    del_row.grid(row = 3, column= 1, sticky= W )
    e_del = Entry(framel3)
    e_del.grid(row=3, column= 2)
    del_button = Button(framel3, text = "Delete row", command = delete_error)
    del_button.grid(row=3, column= 4)

    #ghost labels used
    Label(framel3, text = "          " ).grid(row=3, column= 5 )
    Label(framel3, text = "          " ).grid(row=3, column= 6 )
    Label(framel3, text = "          " ).grid(row=3, column= 7 )
    Label(framel3, text = "          " ).grid(row=3, column= 9 )
    Label(framel3, text = "          " ).grid(row=3, column= 10 )
    
    #excecute buttons within frame 3
    append_b = Button(framel3, text = "Append details", command= input_check)
    append_b.grid(row=3, column=8)
    print_b = Button(framel3, text = "Print details", command= print_details)
    print_b.grid(row = 3, column=12)

 
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
    #total entries varriable will be added by 1
    total_entries += 1    

#Function used to check error on the delete row
def delete_error():
    #global varriables used
    global e_del, total_entries
    #varriable that checks errors
    check = 0
    #if nothing is entered into delete entry
    try:
        if len(e_del.get()) == 0:
        #message box will appear
            messagebox.showerror("Delete Row", "please enter a row number")
        #error check will equal 1
            check = 1
    #if a row number that doesn't exist get's entered 
        if int(e_del.get()) >= total_entries:
            #message box will appear
            messagebox.showerror("Delete Row", "That row does not exist")
            #error check will equal 1
            check = 1
    except:
        messagebox.showerror("Delete Row", "Only integers must be entered in this entry")
        #error check will equal 1
        check = 1


    #if error varriable remains 0
    if check == 0:
        #the delete button function will be excecuted
        delete_button()



def delete_button():
    #Global varriables used
    global customer_details, e_del, total_entries, name_count, framel2
    #code used to get the row number from delete entry
    del customer_details[int(e_del.get())]
    total_entries = total_entries -1
    #deletes the input within delete entry
    e_del.delete(0 ,END)
#Ghost labels that cover labels as they are deleted
    Label(framel2, text="                                ", bg = "white").grid(column=0,row=name_count+7) 
    Label(framel2, text="                                ", bg = 'white').grid(column=2,row=name_count+7)
    Label(framel2, text="                                ", bg = "white").grid(column=4,row=name_count+7)
    Label(framel2, text="                                ", bg = "white").grid(column=6,row=name_count+7)
    Label(framel2, text="                                ", bg = "white").grid(column=8,row=name_count+7)

    print_details()
    #grids used to fix frame 2 positioning
    quit_b.grid(row = 0, column= 0 )
    framel.grid(row= 1, column=0)
    framel2.grid(row= 2, column= 0 )
    framel2.grid(row= 2, column= 0, padx = 20, pady = 20, ipadx = 80, ipady= 100, sticky=N)


#quit button function
def quit_button():
    #global varriable used
    global quit_b
    #quit button creation
    quit_b = Button(root, text = "quit" , command = quit, padx = 30)
    #quit button positioning
    quit_b.grid(column=1, row= 0, sticky= W ) 




  
#Main function that displays program
def main():
    #global varriables used
    global root, customer_details, total_entries
    quit_button()
    #the ammount of entries being printed
    total_entries = 0
    #details list
    customer_details = []
    frame_1()
    frame_2()
    frame3()
    root.mainloop()


main()
