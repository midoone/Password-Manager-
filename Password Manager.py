mport tkinter as tk


def master_key(user_key):

    test_key ='ahmed'
    if test_key != user_key:
        make_window()
    else:
        return print("Welcome")
def make_window():
    window = tk.Toplevel(root)
    tk.Label(window, text='WRONG KEY\n close the window and try again ').pack(padx=30, pady=30)


root = tk.Tk()
root.title("Password Manager")

canvas = tk.Canvas(root, height=300, width=400)
canvas.pack()

button = tk.Button (root, text="Log in", bg='#80c1ff', bd=5, command=lambda: master_key(entry.get()))
button.place(relx=0.3, rely=0.45)

entry = tk.Entry(root)
entry.place(relx=0.3, rely=0.40, relwidth=0.5, relheight=0.05)

label = tk.Label (root, text="Master Key", bg='#80c1ff', bd=5)
label.place(relx=0.3, rely=0.35, relwidth=0.5, relheight=0.05)



root.mainloop()