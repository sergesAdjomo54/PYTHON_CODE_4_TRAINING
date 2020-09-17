from tkinter import ttk
from tkinter import *
import os
from PIL import Image, ImageTk
import sqlite3
from tkinter.dialog import Dialog
from tkinter import commondialog
import fnmatch

profile = {1:''}

def add_customer():
    name = entryName.get()
    phone = entryPhone.get()
    more = entryMore.get()
    
    # create connection
    conn = sqlite3.connect('dbSqlite/database.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO customers('name', 'phone', 'moreinfo') values (?,?,?)", (name, phone, more))
    conn.commit()
    conn.close()
    
    # display connection ON INTERFACE
    conn = sqlite3.connect('dbSqlite/database.db')
    cur = conn.cursor()
    req = cur.execute("SELECT * FROM customers ORDER BY ID DESC")
    req = list(req)
    tree.insert('', END, values = req[0])
    conn.close()
    conn = sqlite3.connect('dbSqlite/database.db')
    cur = conn.cursor()
    req = cur.execute("SELECT * FROM customers ORDER BY ID DESC")
    req = list(req)    
    id = req[0][0]
    filename = entryPhoto.get()
    im = Image.open(filename)
    rgb_im = im.convert('RGB')
    rgb_im.save(("images/profile_" + str(id) + "." + "jpg"))
    conn.close()
    
    
# delete function
def delete_customer():
    idSelect = tree.item(tree.selection())['values'][0]
    conn = sqlite3.connect('dbSqlite/database.db')
    cur = conn.cursor()
    delete = cur.execute("DELETE FROM customers WHERE id = {}".format(idSelect))
    conn.commit()
    tree.delete(tree.selection())
    

# Method sort
def sortByName():
    # clear the treeview
    for x in tree.get_children():
        tree.delete(x)
    #create connection
    conn = sqlite3.connect('dbSqlite/database.db')
    cur = conn.cursor()
    select = cur.execute("SELECT * FROM customers ORDER BY name asc ")
    conn.commit()          
    for row in select:
        tree.insert('', END, values = row)
    conn.close()
    
# Method sorti
def sorti():
    exit()
    

# Load image user Method      
def BrowsePhoto():
    entryPhoto.delete(0, END)
    filename = filedialog.askopenfilename(initialdir ="/", title ="Select File")
    entryPhoto.insert(END, filename)

def treeActionSelect(event):
    #load image
    lbl_Image.destroy()
    
    idSelect = tree.item(tree.selection())['values'][0]
    nameSelect = tree.item(tree.selection())['values'][1]
    phoneSelect = tree.item(tree.selection())['values'][2]
    moreInfoSelect = tree.item(tree.selection())['values'][3]
    
    imgProfile = "images/profile_" + str(idSelect) + "." + "jpg"
    load = Image.open(imgProfile)
    load.thumbnail((100,100))
    photo = ImageTk.PhotoImage(load)
    
    profile[1] = photo
    lblImage = Label(root, image = photo)
    lblImage.place(x = 10, y = 350)
    
    lid = Label(root, text = "ID : " + str(idSelect))
    lid.place(x = 110, y = 350)
    lname = Label(root, text =" Name : " + nameSelect)
    lname.place(x = 110, y = 380)
    lphone = Label(root, text ="Phone : " + str(phoneSelect))
    lphone.place(x = 110, y = 410)
    Tmore = Text(root)
    Tmore.place(x = 260, y = 360, width = 280, height = 100)
    Tmore.insert(END, "More Info : " + moreInfoSelect)
    


root = Tk()
root.title("Adress Book")
root.geometry("550x480")

lbltitle = Label(root, text="Adress Book", font=("Arial"), bg = "violet", fg ="white" )
lbltitle.place(x = 0, y = 0, width = 200)

# Search Area
lbSearchByName = Label(root, text = "Search by Name:", bg="green", fg="white")
lbSearchByName.place(x = 250, y = 0, width = 120)
EntrySearchByName = Entry(root)
EntrySearchByName.place (x = 380, y = 0, width =160)


lbSearchByPhone = Label(root, text = "Search by Phone:", bg="green", fg="white")
lbSearchByPhone.place(x = 250, y = 20, width = 120)
EntrySearchByPhone = Entry(root)
EntrySearchByPhone.place (x = 380, y = 20, width =160)

# Label Name and Surname
lblName = Label(root, text ="Name & Surname:", bg ="gray", fg="yellow")
lblName.place (x = 5, y = 50, width = 125)
entryName = Entry(root)
entryName.place(x=140, y = 50, width = 400)

# Label and Entry phone
lblPhone = Label(root, text ="Phone Number:", bg ="gray", fg ="yellow")
lblPhone.place(x = 5, y = 80, width = 125)
entryPhone = Entry(root)
entryPhone.place(x = 140, y = 80, width = 400)

#Label & Entry photo
lblPhoto = Label(root, text = "Photo:", bg ="gray", fg ="white")
lblPhoto.place(x = 5, y = 110, width = 115)
btnPhoto = Button(root, text = "Browse", bg ="gray", fg ="white", command = BrowsePhoto)
btnPhoto.place(x = 480, y = 110, height = 25, width = 60)
entryPhoto = Entry(root)
entryPhoto.place(x = 140, y = 110, width = 320)

# More infos
lblMore = Label(root, text ="More Infos:", bg ="gray", fg ="yellow")
lblMore.place(x = 5, y = 140, width = 125)
entryMore = Entry(root)
entryMore.place(x = 140, y = 140, width = 400)

# Commande Button
btnAdd = Button(root, text ="ADD CUSTOMER", bg ="orange" , fg ="white", command = add_customer)
btnAdd.place(x = 5, y = 170, width = 255)

btnDelete = Button(root, text ="Delete Selected", bg ="orange" , fg ="white", command = delete_customer)
btnDelete.place(x = 5, y = 205, width = 255)

btnEdit = Button(root, text ="Edit Selected", bg ="orange" , fg ="white")
btnEdit.place(x = 5, y = 240, width = 255)

btnSort = Button(root, text ="Sort by Name", bg ="orange" , fg ="white", command = sortByName)
btnSort.place(x = 5, y = 275, width = 255)

btnExit = Button(root, text ="Exit App", bg ="orange" , fg ="white", command = quit)    
btnExit.place(x = 5, y = 310, width = 155)

# load image
load = Image.open("images/0.gif")
load.thumbnail((130,130))
photo = ImageTk.PhotoImage(load)
lbl_Image = Label(root, image = photo)
lbl_Image.place( x = 10, y = 350)


# add TreeView
tree = ttk.Treeview(root, columns = (1,2,3), height = 5, show = "headings")
tree.place(x = 265, y = 170, width =290, height = 175)
tree.bind("<<TreeviewSelect>>", treeActionSelect)


# Add Headingfrom tkinter.dialog import Dialog
tree.heading(1, text="ID")
tree.heading(2, text="Name")
tree.heading(3, text="Phone")

# Define columns width
tree.column(1, width = 50)
tree.column(2, width = 100)

#Display data in treeview object
conn = sqlite3.connect('dbSqlite/database.db')
cur = conn.cursor()
req = cur.execute("select * from customers")
for row in req:
    tree.insert('' , END , value = row)
conn.close()


root.mainloop()