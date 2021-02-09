from tkinter import *
import os


def check_username():
    global screen6
    list_of_files1 = os.listdir()
    username_info1 = username.get()
    if username_info1 in list_of_files1:
        screen6 = Toplevel(screen)
        screen6.title("Username is taken")
        Label(screen6, text="").pack()
        Label(screen6, text="Username is taken please enter another").pack()
        Label(screen6, text="").pack()
        Button(screen6, text="OK", command=delete5).pack()
    else:
        create_user()


def create_user():
    username_info = username.get()
    password_info = password.get()
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration complete", fg="green", font=("Calibri", 11)).pack()


def new_user():
    global screen1, username, password, username_entry, password_entry
    screen1 = Toplevel(screen)
    screen1.title("Create new account")
    screen1.geometry("300x250")

    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(text="").pack()
    Label(screen1, text="Username").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(text="").pack()
    Button(screen1, text="Register", height="1", width="10", command=check_username).pack()


def delete2():
    screen9.destroy()
    screen8.destroy()


def delete3():
    screen4.destroy()


def delete4():
    screen5.destroy()


def delete5():
    screen6.destroy()


def saved():
    global screen9
    screen9 = Toplevel(screen)
    screen9.title("Saved")
    screen9.geometry("300x250")
    Label(screen9, text="Saved").pack()
    Button(screen9, text="OK", command=delete2).pack()


def save():
    filename = raw_filename.get()
    file = raw_file.get()

    data = open(filename, "w")
    data.write(file)
    data.close()
    saved()


def create_file():
    global raw_filename, raw_file, screen8
    raw_filename = StringVar()
    raw_file = StringVar()
    screen8 = Toplevel(screen)
    screen8.title("Info")
    screen8.geometry("300x250")
    Label(screen8, text="Please enter a filename below: ").pack()
    Entry(screen8, textvariable=raw_filename).pack()
    Label(screen8, text="Please enter the file below: ").pack()
    Entry(screen8, textvariable=raw_file).pack()
    Button(screen8, text="Save", command=save).pack()


def view_file1():
    filename1 = raw_filename1.get()
    data = open(filename1, "r")
    data1 = data.read()
    screen11 = Toplevel(screen)
    screen11.title("Notes")
    screen11.geometry("300x250")
    Label(screen11, text=data1).pack()
    data.close()


def view_file():
    global raw_filename1
    raw_filename1 = StringVar()
    screen10 = Toplevel(screen)
    screen10.title("Info")
    screen10.geometry("300x250")
    all_files = os.listdir()
    Label(screen10, text="Please use one of the filenames below: ").pack()
    Label(screen10, text=all_files).pack()
    Entry(screen10, textvariable=raw_filename1).pack()
    Button(screen10, text="OK", command=view_file1).pack()


def delete_file1():
    filename3 = raw_filename2.get()
    os.remove(filename3)
    screen13 = Toplevel(screen)
    screen13.title("Notes")
    screen13.geometry("300x250")
    Label(screen13, text=filename3 + " deleted").pack()


def delete_file():
    global raw_filename2
    raw_filename2 = StringVar()
    screen12 = Toplevel(screen)
    screen12.title("Info")
    screen12.geometry("300x250")
    all_files = os.listdir()
    Label(screen12, text="Please use one of the filenames below: ").pack()
    Label(screen12, text=all_files).pack()
    Entry(screen12, textvariable=raw_filename2).pack()
    Button(screen12, text="OK", command=delete_file1).pack()


def session():
    screen2.destroy()
    screen7 = Toplevel(screen)
    screen7.title("Dashboard")
    screen7.geometry("400x400")
    Label(screen7, text="Welcome to the dashboard").pack()
    Label(screen7, text="").pack()
    Button(screen7, text="Create file", command=create_file).pack()
    Label(screen7, text="").pack()
    Button(screen7, text="View file", command=view_file).pack()
    Label(screen7, text="").pack()
    Button(screen7, text="Delete file", command=delete_file).pack()


def incorrect_password():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Incorrect password")
    screen4.geometry("300x250")
    Label(screen4, text="Incorrect password").pack()
    Button(screen4, text="OK", command=delete3).pack()


def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("User not found")
    screen5.geometry("300x250")
    Label(screen5, text="User not found").pack()
    Button(screen5, text="OK", command=delete4).pack()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            session()
        else:
            incorrect_password()
    else:
        user_not_found()


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    global username_verify, password_verify, username_entry1, password_entry1
    username_verify = StringVar()
    password_verify = StringVar()
    Label(screen2, text="Please enter details below to login").pack()
    Label(text="").pack()
    Label(screen2, text="Username").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="Password").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(text="").pack()
    Button(screen2, text="Login", height="1", width="10", command=login_verify).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("File system")
    Label(text="File system", bg="grey", height="2", width="300", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Create new account", height="2", width="30", command=new_user).pack()

    screen.mainloop()


main_screen()
