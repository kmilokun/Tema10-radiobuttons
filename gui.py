import tkinter
from tkinter import ttk


def comando():
    actual.config(text=f"Opcion {selec.get()}")


def reiniciar():
    actual.config(text='')


window = tkinter.Tk()
window.title('GUI')

window.columnconfigure(0, weight=2)
window.rowconfigure(0, weight=2)
window.rowconfigure(1, weight=2)
window.rowconfigure(2, weight=2)

selec = tkinter.StringVar()
b1 = tkinter.Radiobutton(window, variable=selec, text='Opcion 1', value=1, command=comando, )
b2 = tkinter.Radiobutton(window, variable=selec, text='Opcion 2', value=2, command=comando, )
b3 = tkinter.Radiobutton(window, variable=selec, text='Opcion 3', value=3, command=comando, )

b1.grid(column=0, row=0)
b2.grid(column=0, row=1)
b3.grid(column=0, row=2)

actual = tkinter.Label(window)
actual.grid(column=0, row=3)

tkinter.Button(text='Reiniciar', command=reiniciar).grid(column=0, row=4)

window.mainloop()
