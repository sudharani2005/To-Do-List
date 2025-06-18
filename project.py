import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task!")

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])
        tasks.pop(selected[0])
    else:
        messagebox.showwarning("Warning", "No task selected!")

# GUI Setup
root = tk.Tk()
root.title("To-Do List App")
root.geometry("300x400")

frame = tk.Frame(root)
frame.pack(pady=20)

listbox = tk.Listbox(frame, width=25, height=10, font=("Arial", 12))
listbox.pack()

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack(pady=5)

del_btn = tk.Button(root, text="Delete Task", command=delete_task)
del_btn.pack(pady=5)

root.mainloop()
