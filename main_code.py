# Task: Creates a payment management application for the residents of a block
# The application must contain a graphical interface and a database
# all users must be stored in the database and if they are not registered in the database, be able to register
#


# Imported relevant modules
from database_interface import Databases
from tkinter import *

root = Tk()
root.title('                                                - Administrator01-')

root.geometry("800x500")
root.config(background="gray")

data1 = Databases("C:/Users/Gabi/PycharmProjects/despa/Administration_app\database.json")
data_info = data1.read_data()


def autentification():
    '''
    this function is used for user login
    :return: none
    '''
    username = user.get()
    pasword = password.get()
    for lista in data_info.values():
        for dictionar in lista:
            if username == dictionar["user"] and pasword == dictionar["password"]:
                name.config(text=f'Your name is: {dictionar["name"]}')
                address.config(text=f'Your adress is: {dictionar["address"]}')
                balance.config(text=f' Balance sheet is: {dictionar["balance"]} ron ')
                status.config(text=f'Welcome {dictionar["name"]}')
                break
            else:
                status.config(text="This user is not registered, try to register")


def pay():
    '''
    this function is used to save the payment made by the user
    :return: none (a new value in database)
    '''
    username = user.get()
    pay = payment.get()
    for lista in data_info.values():
        for dictionar in lista:
            if username == dictionar["user"]:
                print(f' Balance sheet is: {dictionar["balance"]} ron ')
                dictionar["balance"] -= int(pay)
                print(f' Balance sheet is: {dictionar["balance"]} ron ')
                balance.config(text=f' Balance sheet is: {dictionar["balance"]} ron ')
    data1.save_data(data_info)


def register():
    '''
    this function can register a new person in the database,
    if she doesn't exist
    :return: dictionary
    '''
    dictionar = {}
    dictionar["user"] = new_user.get()
    dictionar["password"] = new_password.get()
    dictionar["address"] = new_address.get()
    dictionar["name"] = new_name.get()
    dictionar["balance"] = int(new_balance.get())
    print(dictionar)
    for lista in data_info.values():
        lista.append(dictionar)
    data1.save_data(data_info)
    new_user.delete(0, END)
    new_password.delete(0, END)
    new_address.delete(0, END)
    new_name.delete(0, END)
    new_balance.delete(0, END)


def logout():
    '''
    this function is used to log out
    :return: none
    '''
    user.delete(0, END)
    password.delete(0, END)
    payment.delete(0, END)
    new_user.delete(0, END)
    new_password.delete(0, END)
    new_address.delete(0, END)
    new_name.delete(0, END)
    new_balance.delete(0, END)
    status.config(text='Offline')
    name.config(text="Name")
    address.config(text="Address")
    balance.config(text="balance")


# buttons
login = Button(root, padx=5, pady=10, text="Login", font=10, bg='green', fg='white',
               borderwidth=15, activebackground="green", activeforeground="white", command=autentification)
pay_button = Button(root, padx=5, pady=10, text="PAY", font=10, bg='green', fg='white', borderwidth=15, command=pay)
Register = Button(root, padx=5, pady=10, text="Register", font=10, bg='green', fg='white',
                  borderwidth=15, activebackground="green", activeforeground="white", command=register)
logout = Button(root, padx=5, pady=10, text="Logout", font=10, bg='red', fg='white',
                borderwidth=15, activebackground="yellow", activeforeground="white", command=logout)

login.grid(row=11, column=1)
pay_button.grid(row=11, column=3, padx=5, pady=5)
Register.grid(row=11, column=2, padx=5, pady=5)
logout.grid(row=12, column=3)

# Entry fields
user = Entry(root, width=40)
user.grid(row=1, column=1)
password = Entry(root, width=40, show="*")
password.grid(row=3, column=1)
payment = Entry(root, width=40)
payment.grid(row=4, column=3)
new_user = Entry(root, width=40)
new_user.grid(row=2, column=2)
new_password = Entry(root, width=40)
new_password.grid(row=4, column=2)
new_address = Entry(root, width=40)
new_address.grid(row=6, column=2)
new_name = Entry(root, width=40)
new_name.grid(row=8, column=2)
new_balance = Entry(root, width=40)
new_balance.grid(row=10, column=2)

# labels
username = Label(root, font=30, width=20, bg="white", fg="green", text='Username')
username.grid(row=0, column=1, padx=5, pady=5)
pasword = Label(root, font=30, width=20, bg="white", fg="green", text='Password')
pasword.grid(row=2, column=1, padx=5, pady=5)
status = Label(root, font=30, width=30, bg="white", fg="green", text='Offline')
status.grid(row=4, column=1)
name = Label(root, font=30, width=30, bg="white", fg="green", text='Name')
name.grid(row=1, column=3, padx=5, pady=5)
balance = Label(root, font=30, width=30, bg="white", fg="green", text='Balance')
balance.grid(row=3, column=3, padx=5, pady=5)
address = Label(root, font=30, width=30, bg="white", fg="green", text='Address')
address.grid(row=2, column=3, padx=5, pady=5)
registration = Label(root, font=30, width=20, bg="white", fg="green", text='Register')
registration.grid(row=0, column=2, padx=5, pady=5)
n_user = Label(root, font=30, width=20, bg="white", fg="green", text='Username')
n_user.grid(row=1, column=2)
n_password = Label(root, font=30, width=20, bg="white", fg="green", text='Password')
n_password.grid(row=3, column=2, padx=5, pady=5)
n_address = Label(root, font=30, width=20, bg="white", fg="green", text='Address')
n_address.grid(row=5, column=2, padx=5, pady=5)
n_name = Label(root, font=30, width=20, bg="white", fg="green", text='Name')
n_name.grid(row=7, column=2, padx=5, pady=5)
n_balance = Label(root, font=30, width=20, bg="white", fg="green", text='Balance')
n_balance.grid(row=9, column=2, padx=5, pady=5)

root.mainloop()
