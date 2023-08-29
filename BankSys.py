from tkinter import*
from tkinter import messagebox
import os


def balance():
    os.chdir(os.path.join(currentdir, "balance"))
    balMenu=Tk()
    balMenu.title("Balance")
    balMenu.geometry("350x300")
    balLabel=Label(balMenu, text="Your balance:", font=("Times New Roman", 20))
    balLabel.place(relx=0.5, rely=0.2, anchor=CENTER)
    #Read balance
    file_bal=open(name+".txt", "r")
    bal=file_bal.read()
    balValue=Label(balMenu, text="$"+bal, font=("Times New Roman", 20))
    balValue.place(relx=0.5, rely=0.5, anchor=CENTER)
    file_bal.close()
    os.chdir(currentdir)

def addfunds():
    os.chdir(os.path.join(currentdir, "balance"))
    afundsMenu=Tk()
    afundsMenu.title("Add Funds")
    afundsMenu.geometry("350x300")
    funds_label=Label(afundsMenu, text="Select the amount you want to add:", font=("Times New Roman", 17))
    funds_label.place(relx=0.5, rely=0.25, anchor=CENTER)
    amounts_label=Label(afundsMenu, text="AMOUNT: $", font=("Times New Roman", 15))
    amounts_label.place(relx=0.22, rely=0.5, anchor=CENTER)
    amounts=Entry(afundsMenu)
    amounts.place(relx=0.6, rely=0.5, anchor=CENTER, width=150, height=25)
    #Confirm
    def add():
        file_bal=open(name+".txt", "r")
        oldbal=file_bal.read()
        newbal=amounts.get()
        oldbal=oldbal.strip(" ")
        newbal=newbal.strip(" ")
        if len(newbal)!=0 and newbal.isnumeric()==True:
            if int(newbal)>0:
                bal=int(oldbal)+int(newbal)
                file_bal.close()
                file_bal=open(name+".txt", "w")
                file_bal.write(str(bal))
                messagebox.showinfo("Complete", "Funds added successfully")
                file_bal.close()
                afundsMenu.destroy()
                os.chdir(currentdir)
            else:
                messagebox.showwarning("Error", "Please enter a valid ammount")
        else:
            messagebox.showwarning("Error", "Please enter a valid ammount")
            file_bal.close()

    confirmButton=Button(afundsMenu, text="CONFIRM", font=("Times New Roman", 12), command=add)
    confirmButton.place(relx=0.5, rely=0.8, anchor=CENTER)

def send_money():
    sendMenu=Tk()
    sendMenu.title("Send Money")
    sendMenu.geometry("450x350")
    label=Label(sendMenu, text="SEND MONEY", font=("Times New Roman", 20))
    label_1=Label(sendMenu, text="To who?", font=("Times New Roman", 15))
    label_2=Label(sendMenu, text="How much?", font=("Times New Roman", 15))
    label_3=Label(sendMenu, text="Name", font=("Times New Roman", 15))
    label_4=Label(sendMenu, text="$", font=("Times New Roman", 15))
    label.place(relx=0.51, rely=0.1, anchor=CENTER)
    label_1.place(relx=0.3, rely=0.3, anchor=CENTER)
    label_2.place(relx=0.3, rely=0.6, anchor=CENTER)
    label_3.place(relx=0.06, rely=0.4, anchor=CENTER)
    label_4.place(relx=0.09, rely=0.7, anchor=CENTER)
    receiver_entry=Entry(sendMenu)
    amount_entry=Entry(sendMenu)
    receiver_entry.place(relx=0.46, rely=0.4, anchor=CENTER, width=300, height=30)
    amount_entry.place(relx=0.46, rely=0.7, anchor=CENTER, width=300, height=30)
    #Send
    def send():
        global receiver
        global amount
        os.chdir(os.path.join(currentdir, "balance"))
        #Get balance
        file_sender=open(name+".txt", "r")
        file_receiver=open(receiver+".txt", "r")
        sender_money=file_sender.read()
        receiver_money=file_receiver.read()
        sender_bal=int(sender_money)-int(amount)
        receiver_bal=int(receiver_money)+int(amount)
        file_sender.close()
        file_receiver.close()
        if sender_bal>=0:
            #Subtract sender's money
            file_sender=open(name+".txt", "w")
            file_sender.write(str(sender_bal))
            file_sender.close()
            #Add receiver's money
            file_receiver=open(receiver+".txt", "w")
            file_receiver.write(str(receiver_bal))
            file_receiver.close()
            messagebox.showinfo("Success", "Tranferred successfully")
            sendMenu.destroy()
        else:
            messagebox.showwarning("Error", "Insufficient balance")
    #Re-enter password
    def re_enter():
        #Re enter password
        re_enterMenu=Tk()
        re_enterMenu.title("")
        re_enterMenu.geometry("350x200")
        re_enter_label=Label(re_enterMenu, text="Please re-enter your password", font=("Times New Roman", 12))
        re_enter_input=Entry(re_enterMenu)
        re_enter_label.place(relx=0.5, rely=0.15, anchor=CENTER)
        re_enter_input.place(relx=0.5, rely=0.3, anchor=CENTER)
        def get_re_enter_pass():
            pass_re_enter=re_enter_input.get()
            if pass_re_enter.split()==password.split():
                re_enterMenu.destroy()
                send()
            else:
                re_enterMenu.destroy()
                messagebox.showwarning("Error", "Invalid credentials")

        confirmButton=Button(re_enterMenu, text="CONFIRM", font=("Times New Roman", 10), command=get_re_enter_pass)
        confirmButton.place(relx=0.5, rely=0.6, anchor=CENTER)
    #Checking
    def check():
        global receiver
        global amount
        found=0
        receiver=receiver_entry.get()
        amount=amount_entry.get()
        #Check name
        os.chdir(currentdir)
        file_name=open("name.txt")
        if (" " in receiver)==False and len(receiver)!=0:
            for i in file_name:
                if i.split()==receiver.split() and receiver.split()!= name.split():
                    found=1
                    break
                if i.split()==receiver.split() and receiver.split()== name.split():
                    found=2
                    break
            file_name.close()
        if found==0:
            messagebox.showwarning("Error", "User not found")
        if found==2:
            messagebox.showwarning("Error", "You cannot send yourself")
        if found==1 and len(amount)!=0 and amount.isnumeric()==True and (" " in amount)==False and int(amount)>0:
            re_enter()
        elif len(amount)==0 or amount.isnumeric()==False or (" " in amount)==True or int(amount)<=0:
            messagebox.showwarning("Error", "Please enter a valid amount")

    nextButton=Button(sendMenu, text="NEXT", font=("Times New Roman", 12), command=check)
    nextButton.place(relx=0.5, rely=0.9, anchor=CENTER)

def mainmenu():
    menu=Tk()
    menu.title("Bank")
    menu.geometry("600x500")
    menuLabel=Label(menu, text="WELCOME "+name+"!", font=("Times New Roman", 20))
    exitButton=Button(menu, text="EXIT", font=("Times New Roman", 13), command=menu.destroy)
    exitButton.place(relx=0.5, rely=0.85, anchor=CENTER)
    menuLabel.place(relx=0.5, rely=0.1, anchor=CENTER)
    #Balance
    balButton=Button(menu, text="Check your balance", font=("Times New Roman", 15), command=balance)
    balButton.place(relx=0.3, rely=0.4, anchor=CENTER)
    #Add Funds
    addfundsButton=Button(menu, text="Add Funds", font=("Times New Roman", 15), command=addfunds)
    addfundsButton.place(relx=0.7, rely=0.4, anchor=CENTER)
    #Wire tranfer
    wiretransferButton=Button(menu, text="Wire Transfer", font=("Times New Roman", 15), command=send_money)
    wiretransferButton.place(relx=0.5, rely=0.6, anchor=CENTER)

def shpass():
    global count
    global password_input
    if count==0:
        password_input.destroy()
        password_input=Entry(gui, show="")
        password_input.place(relx=0.55, rely=0.43, anchor=CENTER)
        count=1
    elif count==1:
        password_input.destroy()
        password_input=Entry(gui, show="*")
        password_input.place(relx=0.55, rely=0.43, anchor=CENTER)
        count=0

#Login and Register
#
#Login
def login():
    name=name_input.get()
    password=password_input.get()



#Register
def register():
    global name
    global password
    global name_input
    global password_input
    taken=0
    name=name_input.get()
    password=password_input.get()
    file_name=open("name.txt", "r+")
    file_password=open("password.txt", "a")
    for i in file_name:
        if i.split()==name.split():
            taken=1
            messagebox.showwarning("Warning", "Username already taken")
            file_name.close()
            file_password.close()
            break
    if (" " in name)==False and (" " in password)==False and len(name)!=0 and len(password)!=0 and taken!=1:
        file_name.write(name+"\n")
        file_password.write(password+"\n")
        file_name.close()
        file_password.close()
        messagebox.showinfo("Success", "Registered successfully")
        #Create Balance
        os.chdir(os.path.join(currentdir, "balance"))
        file_bal=open(name+".txt", "w")
        file_bal.write("0")
        file_bal.close()
        os.chdir(currentdir)
        if count==0:
            name_input.destroy()
            name_input=Entry(gui)
            name_input.place(relx=0.55, rely=0.3, anchor=CENTER)
            password_input.destroy()
            password_input=Entry(gui, show="*")
            password_input.place(relx=0.55, rely=0.43, anchor=CENTER)
        elif count==1:
            name_input.destroy()
            name_input=Entry(gui)
            name_input.place(relx=0.55, rely=0.3, anchor=CENTER)
            password_input.destroy()
            password_input=Entry(gui, show="")
            password_input.place(relx=0.55, rely=0.43, anchor=CENTER)
    elif (" " in name) or (" " in password)==True:
        if(" " in name)==True:
            messagebox.showwarning("Warning", "Username must not contain a space")
            file_name.close()
            file_password.close()
        if (" " in password)==True:
            messagebox.showwarning("Warning", "Password must not contain a space")
            file_name.close()
            file_password.close()
    elif len(name)==0 or len(password)==0:
        messagebox.showwarning("Warning", "Username/Password must not be blank")
        file_name.close()
        file_password.close()


def run():
    count = 0
    name = ''
    password = ''
    receiver = ''
    amount = ''
    currentdir = os.getcwd()

    gui = Tk()
    gui.title("Bank")
    gui.geometry("400x350")
    # Label and Input
    loginLabel = Label(gui, text="Please enter your credentials", font="times 15")
    nameLabel = Label(gui, text="Name")
    passwordLabel = Label(gui, text="Password")
    name_input = Entry(gui)
    password_input = Entry(gui, show="*")
    quitButton = Button(gui, text="QUIT", command=gui.destroy)
    quitButton.config(height=1, width=6)

    loginLabel.place(relx=0.52, rely=0.1, anchor=CENTER)
    nameLabel.place(relx=0.3, rely=0.3, anchor=CENTER)
    passwordLabel.place(relx=0.3, rely=0.43, anchor=CENTER)
    name_input.place(relx=0.55, rely=0.3, anchor=CENTER)
    password_input.place(relx=0.55, rely=0.43, anchor=CENTER)
    quitButton.place(relx=0.5, rely=0.8, anchor=CENTER)

    showhidepass = Checkbutton(gui, text="Show password", command=shpass)
    showhidepass.place(relx=0.55, rely=0.53, anchor=CENTER)

    loginButton = Button(gui, text="LOGIN", command=login)
    loginButton.place(relx=0.42, rely=0.65, anchor=CENTER)

    registerButton = Button(gui, text="REGISTER", command=register)
    registerButton.place(relx=0.6, rely=0.65, anchor=CENTER)

    gui.mainloop()

if __name__=="__main__":
    run()
