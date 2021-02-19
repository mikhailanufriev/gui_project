from tkinter import *
from tkinter.ttk import Combobox
from tkinter import scrolledtext


def clicked():
    lbl.configure(text="Я же просил...")
def clicked2():
    lbl2.configure(text="132456...")

def clicked3():
    res = "Привет {}".format(txt.get())
    lbl.configure(text=res)
    lbl2.configure(text=res)

def rbutton():
    res2 = "радиобуттон"
    lbl2.configure(text=res2)

def rbutton2():
    res2 = "радиобуттон2"
    lbl2.configure(text=res2)

def rbutton3():
    res2 = "радиобуттон3"
    lbl2.configure(text=res2)

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('800x600')
lbl = Label(window, text="Привет", font=("Arial Bold", 10))
lbl.grid(column=0, row=0)

lbl2 = Label(window, text="12345", font=("Arial Bold", 10))
lbl2.grid(column=0  , row=1)

btn = Button(window, text="Не нажимать!", command=clicked)
btn.grid(column=1, row=0)

btn2 = Button(window, text="Кнопка 2", command=clicked2)
btn2.grid(column=1, row=1)

txt = Entry(window, width=10)
txt.grid(column=0, row=3)
txt.focus()
btn3 = Button(window, text="Клик!", command=clicked3)
btn3.grid(column=1, row=3)

combo = Combobox(window)
combo['values'] = (1, 2, 3, 4, 5, "Текст")
combo.current(1)  # установите вариант по умолчанию
combo.grid(column=0, row=4)

chk_state = BooleanVar()
chk_state.set(True)  # задайте проверку состояния чекбокса
chk_state = IntVar()
chk_state.set(0) # False
chk = Checkbutton(window, text='Выбрать', var=chk_state)
chk.grid(column=0, row=5)

selected = IntVar()
rad1 = Radiobutton(window, text='Первый', value=1, command=rbutton)
rad2 = Radiobutton(window, text='Второй', value=2, command=rbutton2)
rad3 = Radiobutton(window, text='Третий', value=3, command=rbutton3)
rad1.grid(column=0, row=6)
rad2.grid(column=1, row=6)
rad3.grid(column=2, row=6)

txt = scrolledtext.ScrolledText(window, width=40, height=10)
txt.grid(column=0, row=7)

txt.insert(INSERT, 'Текстовое поле')

window.mainloop()

