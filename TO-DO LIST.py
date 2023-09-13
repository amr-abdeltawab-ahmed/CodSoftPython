from tkinter import *
from tkinter import messagebox


def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Please enter some task.")


def deleteTask():
    selected_task = lb.curselection()
    if selected_task:
        lb.delete(selected_task)


ws = Tk()
ws.geometry('600x500+500+200')
ws.title('To-Do List App')
ws.config(bg='#34495E')

frame = Frame(ws, bg='#34495E')
frame.pack(pady=10)

lb = Listbox(frame, width=35, height=10, font=('Arial', 18), bd=0, fg='#FFFFFF', selectbackground='#a6a6a6', activestyle="none", bg='#34495E')
lb.pack(side=LEFT, fill=BOTH)

task_list = []

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=Y)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(ws, font=('Arial', 24))
my_entry.pack(pady=20)

button_frame = Frame(ws, bg='#34495E')
button_frame.pack(pady=20)

addTask_btn = Button(button_frame, text='Add Task', font='Arial 14', bg='#2ECC71', padx=20, pady=10, command=newTask)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(button_frame, text='Delete Task', font='Arial 14', bg='#E74C3C', padx=20, pady=10, command=deleteTask)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

ws.mainloop()
