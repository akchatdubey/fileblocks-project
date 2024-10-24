import tkinter as tk
def add():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    result = num1 + num2
    result_entry.delete(0, tk.END)  # Clear the previous result
    result_entry.insert(0, result)
def subtract():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    result = num1 - num2
    result_entry.delete(0, tk.END)  # Clear the previous result
    result_entry.insert(0, result)
root = tk.Tk()
root.geometry("500x500")
root.title("Add and Subtract Two Numbers")
num1_label = tk.Label(root, text="Number 1:")
num1_entry = tk.Entry(root)
num2_label = tk.Label(root, text="Number 2:")

num2_entry = tk.Entry(root)
add_button = tk.Button(root, text="Add", command=add)
subtract_button = tk.Button(root, text="Subtract", command=subtract)

result_label = tk.Label(root, text="Result:")
result_entry = tk.Entry(root)
num1_label.grid(row=0, column=0)
num1_entry.grid(row=0, column=1)
num2_label.grid(row=1, column=0)
num2_entry.grid(row=1, column=1)
add_button.grid(row=2, column=0, pady=10)
subtract_button.grid(row=2, column=1, pady=10)
result_label.grid(row=3, column=0)
result_entry.grid(row=3, column=1)
root.mainloop()
