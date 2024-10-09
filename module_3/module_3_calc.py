import tkinter as tk


def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2


def insert_values(value):
    answer_enry.delete(0, 'end')
    answer_enry.insert(0, value)


def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)


def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)


def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)


def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)


window = tk.Tk()
window.title('Калькулятор')
window.geometry('350x350')
window.resizable(False, False)
button_add = tk.Button(window, text='+', width=2, height=2, command=add)
button_add.place(x=50, y=200)
button_sub = tk.Button(window, text='-', width=2, height=2, command=sub)
button_sub.place(x=115, y=200)
button_mul = tk.Button(window, text='*', width=2, height=2, command=mul)
button_mul.place(x=185, y=200)
button_div = tk.Button(window, text='/', width=2, height=2, command=div)
button_div.place(x=250, y=200)
number1_entry = tk.Entry(window, width=30)
number1_entry.place(x=50, y=80)
number2_entry = tk.Entry(window, width=30)
number2_entry.place(x=50, y=140)
answer_enry = tk.Entry(window, width=30)
answer_enry.place(x=50, y=290)
number1 = tk.Label(window, text='Введите первое число:')
number1.place(x=50, y=53)
number2 = tk.Label(window, text='Введите второе число:')
number2.place(x=50, y=113)
answer = tk.Label(window, text='Ответ:')
answer.place(x=50, y=263)
window.mainloop()