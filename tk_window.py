import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Второй проектэ')
label = tk.Label(root, text='Привет, мир!')
label.pack()

def on_button_click():
    label.config(text ='Кнопка была нажата!')

button = tk.Button(root, text="Нажми меня!", command=on_button_click)
button.pack()

def close_window():
    root.destroy()

close_button = tk.Button(root, text="Закрыть окно", command=close_window)
close_button.pack()

root.mainloop()


