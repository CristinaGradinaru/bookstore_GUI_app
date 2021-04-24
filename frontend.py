import tkinter as tk
import backend

def get_selected_row(event):
    global selected_row
    if len(list1.curselection())> 0:
        index=list1.curselection()[0]
        selected_row=list1.get(index)
        e1.delete(0,tk.END)
        e1.insert(tk.END,selected_row[1])
        e2.delete(0,tk.END)
        e2.insert(tk.END,selected_row[2])
        e3.delete(0,tk.END)
        e3.insert(tk.END,selected_row[3])
        e4.delete(0,tk.END)
        e4.insert(tk.END,selected_row[4])
        return selected_row

def view_command():
    list1.delete(0,tk.END)
    for book in backend.view():
        list1.insert(tk.END,book)

def search_command():
    list1.delete(0,tk.END)
    for book in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(tk.END,book)

def insert_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0,tk.END)
    list1.insert(tk.END,(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_command():
    backend.delete(selected_row[0])

def update_command():
    backend.update(selected_row[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

window = tk.Tk()
window.wm_title("Cristina's BookStore")

l1=tk.Label(window, text='Title')
l1.grid(row=0,column=0)

l2=tk.Label(window, text='Author')
l2.grid(row=0,column=2)

l3=tk.Label(window, text='Year')
l3.grid(row=1,column=0)

l4=tk.Label(window, text='ISBN')
l4.grid(row=1,column=2)

title_text= tk.StringVar()
e1=tk.Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text= tk.StringVar()
e2=tk.Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text=tk.StringVar()
e3=tk.Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text=tk.StringVar()
e4=tk.Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)


list1=tk.Listbox(window, height=6, width=35)
list1.grid(row=2,column=0, rowspan=6, columnspan=2)

sb1=tk.Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1=tk.Button(window, text="View all", width=12, command= view_command)
b1.grid(row=2,column=3)

b2=tk.Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=3,column=3)

b3=tk.Button(window, text="Add entry", width=12, command=insert_command)
b3.grid(row=4,column=3)

b4=tk.Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5,column=3)

b5=tk.Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=6,column=3)

b6=tk.Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()