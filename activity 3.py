from tkinter import *

window = Tk()
window.title('Multiplication Application')
window.geometry('400x300')

title_label = Label(window, text="Enter two numbers to calculate the product", bg="lightblue", fg="black", height=2)
title_label.pack()

label_num1 = Label(window, text="First Number:")
label_num1.pack()
entry_num1 = Entry(window)
entry_num1.pack()

label_num2 = Label(window, text="Second Number:")
label_num2.pack()
entry_num2 = Entry(window)
entry_num2.pack()

def calculate_product():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        product = num1 * num2
        result_box.insert(END, f"Product: {product}\n")
    except ValueError:
        result_box.insert(END, "Invalid input! Please enter valid numbers.\n")

btn_calculate = Button(window, text="Calculate Product", command=calculate_product, bg="green", fg="white", height=2)
btn_calculate.pack()

result_box = Text(window, height=4)
result_box.pack()

window.mainloop()
