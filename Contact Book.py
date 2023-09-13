from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('700x550')
root.config(bg='#3498db')
root.title('Contact Book')
root.resizable(0, 0)

contactlist = []

Name = StringVar()
Phone = StringVar()
Email = StringVar()
Address = StringVar()


def Selected():
    if len(select.curselection()) > 0:
        return int(select.curselection()[0])
    return None


def AddContact():
    name = Name.get()
    phone = Phone.get()
    email = Email.get()
    address = Address.get()
    if name and phone:
        contact = {
            'Name': name,
            'Phone': phone,
            'Email': email,
            'Address': address
        }
        contactlist.append(contact)
        Select_set()
        EntryReset()
        messagebox.showinfo("Confirmation", "Contact added successfully!")
    else:
        messagebox.showerror("Error", "Name and Phone are required fields.")


def UpdateDetail():
    selected_index = Selected()
    if selected_index is not None:
        name = Name.get()
        phone = Phone.get()
        email = Email.get()
        address = Address.get()
        if name and phone:
            contact = {
                'Name': name,
                'Phone': phone,
                'Email': email,
                'Address': address
            }
            contactlist[selected_index] = contact
            messagebox.showinfo("Confirmation", "Contact updated successfully!")
            EntryReset()
            Select_set()
        else:
            messagebox.showerror("Error", "Name and Phone are required fields.")
    else:
        messagebox.showerror("Error", "Please select a contact.")


def Delete_Entry():
    selected_index = Selected()
    if selected_index is not None:
        result = messagebox.askyesno('Confirmation', 'Are you sure you want to delete this contact?')
        if result:
            del contactlist[selected_index]
            Select_set()
            EntryReset()
    else:
        messagebox.showerror("Error", "Please select a contact to delete.")


def VIEW():
    selected_index = Selected()
    if selected_index is not None:
        contact = contactlist[selected_index]
        Name.set(contact['Name'])
        Phone.set(contact['Phone'])
        Email.set(contact['Email'])
        Address.set(contact['Address'])
    else:
        messagebox.showerror("Error", "Please select a contact to view.")


def EntryReset():
    Name.set('')
    Phone.set('')
    Email.set('')
    Address.set('')


def Select_set():
    contactlist.sort(key=lambda x: x['Name'].lower())
    select.delete(0, END)
    for contact in contactlist:
        select.insert(END, contact['Name'])


frame = Frame(root)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('Times new roman', 16), bg="#f0fffc",
                 width=20, height=20, borderwidth=3, relief="groove")
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)

Label(root, text='Name', font=("Times new roman", 25, "bold"), bg='SlateGray3').place(x=30, y=20)
Entry(root, textvariable=Name, width=30).place(x=200, y=30)
Label(root, text='Phone', font=("Times new roman", 22, "bold"), bg='SlateGray3').place(x=30, y=70)
Entry(root, textvariable=Phone, width=30).place(x=200, y=80)
Label(root, text='Email', font=("Times new roman", 22, "bold"), bg='SlateGray3').place(x=30, y=120)
Entry(root, textvariable=Email, width=30).place(x=200, y=130)
Label(root, text='Address', font=("Times new roman", 22, "bold"), bg='SlateGray3').place(x=30, y=170)
Entry(root, textvariable=Address, width=30).place(x=200, y=180)

Button(root, text=" ADD", font='Helvetica 18 bold', bg='#e8c1c7', command=AddContact, padx=20).place(x=50, y=240)
Button(root, text="EDIT", font='Helvetica 18 bold', bg='#e8c1c7', command=UpdateDetail, padx=20).place(x=50, y=300)
Button(root, text="DELETE", font='Helvetica 18 bold', bg='#e8c1c7', command=Delete_Entry, padx=20).place(x=50, y=360)
Button(root, text="VIEW", font='Helvetica 18 bold', bg='#e8c1c7', command=VIEW).place(x=50, y=420)
Button(root, text="RESET", font='Helvetica 18 bold', bg='#e8c1c7', command=EntryReset).place(x=50, y=480)
Button(root, text="EXIT", font='Helvetica 24 bold', bg='tomato', command=root.quit).place(x=250, y=480)

Select_set()

root.mainloop()