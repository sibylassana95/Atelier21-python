from tkinter import*
import sqlite3 

def validate():
    # récupération des données du formulaire
    name = entryName.get()
    email   =  entryEmail.get() 
    age     =  entryAge.get() 
    conn = sqlite3.connect('mydatabase.db')
    cur = conn.cursor()
    req1 = "CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL\
,email TEXT NOT NULL , age INTEGER NOT NULL)"
    cur.execute(req1)    
    req2 = "INSERT INTO students (name , email, age) values (?, ?, ?)"
    cur.execute(req2 , (name, email, age))
    conn.commit()
    conn.close()
    

root = Tk()
root.geometry("600x400")

#==============================
# create a form to insert data
#==============================
# Label & Entry pour le nom
lblName = Label(root , text = "Name : ")
lblName.place(x = 10 , y = 10)
entryName = Entry(root )
entryName.place(x = 100 , y = 10 , width = 200)

# Label & Entry pour l'Email
lblEmail = Label(root , text = "Email")
lblEmail.place( x = 10 , y = 40 ) 
entryEmail = Entry(root)
entryEmail.place( x = 100 , y = 40 , width = 200)

# Label & Entry  pour l'Age
lblAge = Label(root , text = "Age")
lblAge.place( x = 10 , y = 70 ) 
entryAge = Entry(root)
entryAge.place( x = 100 , y = 70 , width = 200)

#  Action du button
btnValidate = Button(root , text = "Validate" , command = validate)
btnValidate.place(x = 100 , y = 100, width = 200 , height = 25)

root.mainloop()
