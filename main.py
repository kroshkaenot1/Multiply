import tkinter
import random
from tkinter import messagebox

ex = []
multiplication = [(2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9),
                  (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9),
                  (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9),
                  (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9),
                  (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9),
                  (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9),
                  (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9),
                  (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9)]
errors = 0


def firstRound():
    global errors
    answer = answerEntry.get()
    if answer == "":
        messagebox.showerror("Ошибка", "Пустой ответ!")
        return
    try:
        answer = int(answer)
    except ValueError:
        messagebox.showerror("Ошибка", "Некорректный ответ!")
        answerEntry.delete(0, tkinter.END)
        return
    Num1 = num1.cget("text")
    Num2 = num2.cget("text")
    if Num1 * Num2 == answer:
        messagebox.showinfo("Умножение", "Ответ верный!")
        multiplication.remove((Num1, Num2))
        answerEntry.delete(0, tkinter.END)
    else:
        messagebox.showerror("Умножение", "Ответ неверный!")
        ex.append((Num1, Num2))
        multiplication.remove((Num1, Num2))
        errors += 1
        countOfErrors.configure(text=errors)
        answerEntry.delete(0, tkinter.END)

    if len(multiplication) == 0:
        confirm.configure(command=secondRound)
        messagebox.showinfo("Умножение", "Первый круг закончен!")
        example = random.choice(ex)
        num1["text"] = example[0]
        num2["text"] = example[1]
        l = tkinter.Label(window, text="Проверка ошибок",font=fonts)
        l["bg"] = "#0776A0"
        l.grid(row=0, columnspan=6)
        return
    example = random.choice(multiplication)
    num1["text"] = example[0]
    num2["text"] = example[1]


def secondRound():
    answer = answerEntry.get()
    if answer == "":
        messagebox.showerror("Ошибка", "Пустой ответ!")
        return
    try:
        answer = int(answer)
    except ValueError:
        messagebox.showerror("Ошибка", "Некорректный ответ!")
        return
    Num1 = num1.cget("text")
    Num2 = num2.cget("text")
    if Num1 * Num2 == answer:
        messagebox.showinfo("Умножение", "Ответ верный!")
        ex.remove((Num1, Num2))
        answerEntry.delete(0, tkinter.END)
    else:
        messagebox.showerror("Умножение", "Ответ неверный!")
        ex.remove((Num1, Num2))
        answerEntry.delete(0, tkinter.END)
    if len(ex) == 0:
        messagebox.showinfo("Умножение", "Упражнение закончено!")
        exit()
    example = random.choice(ex)
    num1["text"] = example[0]
    num2["text"] = example[1]


fonts = ("Arial", 30)
window = tkinter.Tk()
window.title("Практика таблицы умножения")
window.resizable(width=False, height=False)
window["bg"] = "#0776A0"

firstEx = random.choice(multiplication)
num1 = tkinter.Label(window, text=firstEx[0], font=fonts)
num1["bg"] = "#0776A0"
num1.grid(row=1, column=1)

mult = tkinter.Label(window, text="*", font=fonts)
mult["bg"] = "#0776A0"
mult.grid(row=1, column=2)

num2 = tkinter.Label(window, text=firstEx[1], font=fonts)
num2["bg"] = "#0776A0"
num2.grid(row=1, column=3)

eq = tkinter.Label(window, text="=", font=fonts)
eq["bg"] = "#0776A0"
eq.grid(row=1, column=4)

answerEntry = tkinter.Entry(window, width=8)
answerEntry.grid(row=1, column=5)

confirm = tkinter.Button(window, text="Ответить", command=firstRound, font=("Arial",20))
confirm.grid(row=2, column=1, columnspan=5)

errorLabel = tkinter.Label(window, text="Количество ошибок:", font=fonts)
errorLabel["bg"] = "#0776A0"
errorLabel.grid(row=3, column=1, columnspan=5)

countOfErrors = tkinter.Label(window, text=errors, font=fonts)
countOfErrors["bg"] = "#0776A0"
countOfErrors.grid(row=3, column=6)

window.mainloop()