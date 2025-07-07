from tkinter import *
import Figures, Pencils, Shadows
import os
import sys
import sys
import ctypes
myappid = 'mycompany.myapp.1.0'  
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  
    except Exception:
        base_path = os.path.abspath(".")  

    return os.path.join(base_path, relative_path)


root = Tk()
try:
    icon_path = resource_path('Neiros.ico')
    root.iconbitmap(icon_path)
except Exception as e:
    print(f"Ошибка загрузки иконки: {e}")
def play():
    selected_game = var.get()
    root.withdraw()  
    
    if selected_game == 0:
        Figures.fplay(root)
    elif selected_game == 1:
        Pencils.pplay(root)
    elif selected_game == 2:
        Shadows.splay(root)

def show_main_menu():
    root.deiconify()  

def back_to_menu():
    root.deiconify()

def exit_app():
    root.destroy()


root.geometry("1000x1000")
root.title("Выбор игры")
root.configure(bg='#F0E6FF')

button_style = {
    'bg': '#9D4EDD',
    'fg': 'white',
    'activebackground': '#7B2CBF',
    'activeforeground': 'white',
    'bd': 0,
    'relief': 'raised',
    'font': ('Arial', 14, 'bold'),
    'width': 10,
    'height': 2,
    'cursor': 'hand2',
    'highlightthickness': 2,
    'highlightbackground': '#C77DFF',
    'highlightcolor': '#E0AAFF'
}

content_frame = Frame(root, bg='#F0E6FF')
content_frame.pack(pady=20)

title_label = Label(content_frame, text="ВЫБОР ИГРЫ", 
                   font=('Arial', 24, 'bold'), 
                   fg='#C71585', bg='#F0E6FF')
title_label.pack(pady=(0, 10))

Label(content_frame, text='Выберите игру:', 
      font=('Arial', 16), bg='#F0E6FF', fg='#5A189A').pack()

radio_frame = Frame(content_frame, bg='#F0E6FF')
radio_frame.pack(pady=10)

var = IntVar(value=0)

games = [
    ("Фигуры", 0),
    ("Карандаши", 1),
    ("Тени", 2)
]

radio_style = {
    'font': ('Arial', 14),
    'bg': '#F0E6FF',
    'fg': '#5A189A',
    'activebackground': '#F0E6FF',
    'selectcolor': '#E0AAFF',
    'padx': 20,
    'pady': 8
}

for text, value in games:
    Radiobutton(radio_frame, text=text, variable=var, value=value, **radio_style).pack(anchor='w')


button_frame = Frame(content_frame, bg='#F0E6FF')
button_frame.pack(pady=20)

Button(button_frame, text='Применить', command=play, **button_style).pack(side=LEFT, padx=10)
Button(button_frame, text='Выход', command=exit_app, **button_style).pack(side=LEFT, padx=10)


decor_frame = Frame(root, height=4, bg='#C71585')
decor_frame.pack(fill='x', side='bottom', pady=(0, 0))

root.protocol("WM_DELETE_WINDOW", exit_app)
root.mainloop()