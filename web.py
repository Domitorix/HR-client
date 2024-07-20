import tkinter
from tkinter import ttk
from work_db import cur

root = tkinter.Tk()
root.title('HR-client')

root.geometry('1280x720')

notebook = ttk.Notebook()
notebook.pack()

frame_1 = ttk.Frame(notebook)
frame_2 = ttk.Frame(notebook)
frame_1.pack()
frame_2.pack()

notebook.add(frame_1, text='Кандидаты')
notebook.add(frame_2, text="Добавить кандидата")

tab_1 = tkinter.Label(frame_1, text=cur)
tab_2 = tkinter.Label(frame_2, text="Добавить")
tab_1.pack()
tab_2.pack()




root.mainloop()