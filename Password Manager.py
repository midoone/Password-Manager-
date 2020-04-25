import sqlite3
import tkinter as tk


def master_key(user_key):
    test_key='ahmed'
    if test_key != user_key:
        make_window ()
    else:
        return main_window()


def make_window():
    window=tk.Toplevel (root)
    tk.Label (window, text='WRONG KEY\n close the window and try again ').pack (padx=30, pady=30)


def window2():
    window=tk.Toplevel (root)
    tk.Label (window, text=get_user).pack (padx=30, pady=30)


def main_window():
    root=tk.Tk ()
    canvas=tk.Canvas (root, height=300, width=400)
    canvas.pack ()

    button=tk.Button (root, text="Search", bg='#80c1ff', bd=5, command=lambda: select_user(entry1.get ()))
    button.place (relx=0.3, rely=0.45,relwidth=0.15, relheight=0.15)
    button=tk.Button (root, text="Add", bg='#80c1ff', bd=5, command=lambda: insert_user(entry1.get (), entry2.get ()))
    button.place (relx=0.65, rely=0.45, relwidth=0.15, relheight=0.15)

    entry2=tk.Entry (root)
    entry2.place (relx=0.3, rely=0.40, relwidth=0.5, relheight=0.05)
    entry1=tk.Entry (root)
    entry1.place (relx=0.3, rely=0.30, relwidth=0.5, relheight=0.05)

    label=tk.Label (root, text="PassWord", bg='#80c1ff', bd=5)
    label.place (relx=0.3, rely=0.35, relwidth=0.5, relheight=0.05)
    label=tk.Label (root, text="UserName", bg='#80c1ff', bd=5)
    label.place (relx=0.3, rely=0.25, relwidth=0.5, relheight=0.05)




def insert_user(new_username, new_password):
    conn=sqlite3.connect ('user.db')
    c=conn.cursor ()

    c.execute ("INSERT INTO data (username, password) VALUES (?, ?)", (new_username, new_password))
    conn.commit ()
    conn.close ()

    return


def select_user(username_az):
    conn=sqlite3.connect ('user.db')
    c=conn.cursor ()
    conn.commit ()
    c.execute ("SELECT * FROM data WHERE username=:username", {'username': username_az})
    cursor=c.fetchone ()
    print(cursor[1])










root=tk.Tk ()
root.title ("Password Manager")

canvas=tk.Canvas (root, height=300, width=400)
canvas.pack ()

button=tk.Button (root, text="Log in", bg='#80c1ff', bd=5, command=lambda: master_key (entry.get ()))
button.place (relx=0.3, rely=0.45, relwidth=0.15, relheight=0.15)

entry=tk.Entry (root)
entry.place (relx=0.3, rely=0.40, relwidth=0.5, relheight=0.05)

label=tk.Label (root, text="Master Key", bg='#80c1ff', bd=5)
label.place (relx=0.3, rely=0.35, relwidth=0.5, relheight=0.05)

root.mainloop ()
