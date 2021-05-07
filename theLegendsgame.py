# The legends only invest game window

from tkinter import *
import tkinter.messagebox
import os

def bet():
     import random
     secretNumber = random.randint(1,10)
     stake=int(input("ENTER YOUR STAKE:"))
     if stake <10:
          tkinter.messagebox.showinfo("ENTER A VALID AMOUNT")
          sys.exit()
            

   # Ask the player to guess 6 times.
     for guessesTaken in range(1,3):
       print('ENTER YOUR LUCKY NUMBER.')
       guess = int(input())
       if guess < secretNumber:
             print('not correct!!!TRY ANOTHER')
       elif guess > secretNumber:
             print('not correct!!!TRY ANOTHER')
       else:
             break #This condition is the correct guess!
            

     if guess == secretNumber:
                     num_guesses = str(guessesTaken)
                     if num_guesses == 1:
                         print("CONGRATULATIONS you won, "+ str( 4*stake)+ "in your first guess")              
                     else:
                         print("CONGRATULATIONS you won, "+ str(2*stake) + "in 2 guesses")
     else:
                     print('Nope!!!THE LUCKY NUMBER WAS ' + str(secretNumber))
    


def join_now():
     username_info=username.get()
     password_info=password.get()

     file=open(username_info,"w")
     file.write(username_info+"\n")
     file.write(password_info)
     file.close()

     username_entry.delete(0,END)
     password_entry.delete(0,END)
     

def register():
    global root1
    root1 = Toplevel(root)
    root1.title("Register as a new member")
    root.geometry("600x300")
    root1.resizable(0,0)
    
    global username
    global password
    global username_entry
    global password_entry
    username=StringVar()
    password=StringVar()
    
    Label(root1,text="PLEASE ENTER YOUR DETAILS HERE TO REGISTER",background="green",font="calibri 11 bold",fg="white").pack()
    Label(root1,text="").pack()
    Label(root1,text="username",background="green",fg="black").pack()
    
   
    username_entry=Entry(root1,textvariable=username)
    username_entry.pack()
    Label(root1,text="password",background="green").pack()
    password_entry = Entry(root1,textvariable=password)
    password_entry.pack()
    Label(root1,text="").pack()
    Button(root1,text="Registar",width=10,height=1,background="red",command=join_now).pack()
     
def login():
    global root2
    root2=Toplevel(root)
    root2.title("Login")
    root2.geometry("300x250")
    Label(root2,text="Please enter details below to login").pack()
    Label(root2,text="").pack()

    global username_verify
    global password_verify

    username_verify=StringVar()
    password_verify=StringVar()

    global username_entry1
    global password_entry1
    
    Label(root2,text="Username",background="green").pack()
    username_entry1=Entry(root2,textvariable=username_verify)
    username_entry1.pack()
    Label(root2,text="").pack()
    Label(root2,text="password",background="green").pack()
    password_entry1=Entry(root2,textvariable=password_verify)
    password_entry1.pack()
    Label(root2,text="").pack()
    Button(root2,text="Login",width=10,height=1,background="black",fg="white",command=login_verify).pack()

def login_verify():
    username1=username_verify.get()
    password1=password_verify.get()
    username_entry1.delete(0,END)
    password_entry1.delete(0,END)

    list_of_files=os.listdir()
    if username1 in list_of_files:
        file1=open(username1,"r")
        verify=file1.read().splitlines()#read all lines ignoring the blank
        if password1 in verify:
            print("GOODLUCK AS YOU PLACE YOUR BET")
            bet()
        else:
            tkinter.messagebox.showinfo("PASSWORD IS NOT RECOGNIZED!!!")
    else:
        tkinter.messagebox.showinfo("USER NOT FOUND!!!")



#main
root = Tk()
root.title("")
root.configure(background = "green")
root.geometry("650x300")

#create label 1
label1 = Label(text = "THE LEGENDS ONLY INVEST GAME",font="times 13 bold",background="green",fg="black")
label1.grid(row=0,column=2,sticky=W)

#create label 2
label2= Label(text="Terms and conditions apply",font="none 6",background="green",fg="black")
label2.grid(row=1,column=2,sticky=W)

#create label 3
label3 = Label(text="Winners quit quitting",font="none 15 bold",background="green",fg="black")
label3.grid(row=2,column=0,sticky=W)

#create label 4
label4 = Label(root,text="Username:",background="green")
label4.grid(row=5,column=1)

#create Username entry box
entrySpace=Entry(root,background="white")
entrySpace.grid(row=5,column=2)

#create label 5
label5 = Label(root,text="password:",background="green")
label5.grid(row=7,column=1)

#create password entry box
entrySpace2 = Entry(root,background="white")
entrySpace2.grid(row=7,column=2)

#create password checkbox
cbutton=Checkbutton(text="Remember password")
cbutton.grid(columnspan=5)

#create the Join Now button
label6 = Button(text="JOIN NOW",background="grey",fg="white",command=register)
label6.grid(row=3,column=5)

#create the submit button
label7 = Button(text="LOGIN",background="black",fg="white",command=login)
label7.grid(row=10,column=5)

mainMenu=Menu(root)
root.configure(menu=mainMenu)
subMenu=Menu(mainMenu)
mainMenu.add_cascade(label="MENU",menu=subMenu)
subMenu.add_command(label="JOIN NOW",command=register,background="black",foreground="white")
subMenu.add_separator()
subMenu.add_command(label="LOGIN",command=login,background="black",foreground="white")
subMenu.add_separator()
subMenu.add_command(label="PLACE BET",command=bet,background="black",foreground="white")

root.mainloop()


