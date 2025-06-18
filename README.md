# To-Do-List
   The To-Do List Python project is a GUI-based task management application built using the Tkinter library. 
   It allows users to dynamically add, view, and delete tasks with interactive widgets and real-time updates.
# 🔧 Features
   Add new tasks via input field

   Delete selected tasks from the list

   Clean and responsive GUI
# 💡 What I Learned
  Tkinter widgets (Entry, Button, Listbox, Frame)

 Event handling in GUI applications

 Basic data storage using Python lists

 GUI layout and styling techniques
 # ✅ Working of the To-Do List App
  # Input Field
Allows users to enter task names using a text entry box (tk.Entry).

Input is read and cleared upon clicking the Add button.

   # Task Display (Listbox)
Shows all added tasks in a scrollable list format.

Updates dynamically when tasks are added or deleted.

  # Add Button
Adds typed task to the internal list and displays it in the Listbox.

Prevents adding empty tasks with a validation check.

 # Delete Button
Removes the selected task from the Listbox and the internal list.

Warns if no task is selected using a message box.

  # Pop-up Warnings
Alerts users when trying to add an empty task or delete without selection.

Uses messagebox.showwarning() for smooth UX feedback.


