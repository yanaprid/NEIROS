#pencils
from tkinter import *
import random
from math import radians, cos, sin

def pplay(main_root):
    root = Toplevel()
    root.geometry("1000x1000")
    root.title("ВРАЩАЮЩИЕСЯ КАРАНДАШИ")
    root.configure(bg='#F0E6FF')
    canvas_visible = BooleanVar(value=True)
    
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
    
    canvas_frame = Frame(root, bg='#C71585', bd=4, relief='ridge', padx=5, pady=5)
    canvas_frame.pack(side=BOTTOM, pady=(0, 20))

    c = Canvas(canvas_frame, width=900, height=700, bg='white', highlightthickness=0)
    c.pack()
    
    top_frame = Frame(root, bg='#F0E6FF')
    top_frame.pack(fill=X, padx=10, pady=10)

    count_frame = Frame(top_frame, bg='#F0E6FF')
    count_frame.pack(side=RIGHT)

    Label(count_frame, text='Выберите количество:', 
          font=('Arial', 16), bg='#F0E6FF', fg='#5A189A').pack()

    var = IntVar(value=0)
    colvo = [("5", 0), ("6", 1), ("7", 2)]

    for text, value in colvo:
        Radiobutton(count_frame, text=text, variable=var, value=value, 
                   font=('Arial', 14), bg='#F0E6FF', fg='#5A189A',
                   activebackground='#F0E6FF', selectcolor='#E0AAFF').pack(side=LEFT, padx=5)

    colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FFA500', '#8B4513', '#FF00FF']

   
    pencils = []

    def create_pencil(x, y, color, angle=0):
        parts = []
        width, height = 40, 350 
    
        body = c.create_rectangle(x-width/2, y-height/2, x+width/2, y+height/2,
                                 fill=color, outline='black', width=1)
        parts.append(body)
    
        
        wood_start = y-height/2  # Верх корпуса
        wood_end = wood_start - 25
        # дальше отрисовка от корпуса до грифеля
        wood_points = [ 
            x-width/2, wood_start,
            x-width/3, wood_end,
            x+width/3, wood_end,
            x+width/2, wood_start
    
        ]
        
    
        wood = c.create_polygon(wood_points, fill='#DEB887', outline='black', width=1)
        parts.append(wood)
        
        lead_top = wood_end - 40  # Вершина грифеля
    
        lead_points = [
            x-width/3, wood_end,   # Левая точка основания
            x, lead_top,           # Вершина грифеля
            x+width/3, wood_end    # Правая точка основания
        ]
    
        lead = c.create_polygon(lead_points, fill=color, outline='black', width=1)
        parts.append(lead)
    




        for i in range(1, 3):  
            pos = x - width/2 + (width * i/3) 
            stripe = c.create_line(pos, y-height/2, pos, y+height/2-20, 
                                  fill='black', width=1)
            parts.append(stripe)
    
        rotate_parts(parts, x, y, angle)
    
        return {
            'parts': parts,
            'x': x,
            'y': y,
            'width': width,
            'height': height,
            'angle': angle
        }

    def rotate_parts(parts, center_x, center_y, angle):
        rad = radians(angle)
        for part in parts:
            coords = c.coords(part)
            new_coords = []
            for i in range(0, len(coords), 2):
                px, py = coords[i], coords[i+1]
                px -= center_x
                py -= center_y
                new_px = px * cos(rad) - py * sin(rad)
                new_py = px * sin(rad) + py * cos(rad)
                new_coords.extend([new_px + center_x, new_py + center_y])
            c.coords(part, *new_coords)

    def rotate_pencils():
        for pencil in pencils:
            new_angle = pencil['angle'] + 90
            rotate_parts(pencil['parts'], pencil['x'], pencil['y'], 90)
            pencil['angle'] = new_angle

    def shuffle_pencils():
        c.delete("all")
        pencils.clear()
    
        selected = var.get()
        num_pencils = [5, 6, 7][selected]
    
        for i in range(num_pencils):
            while True:
                x = random.randint(100, 800)
                y = random.randint(100, 600)
                color = colors[i % len(colors)]
                angle = random.choice([0, 90, 180, 270])
            
                if (150 < x < 950 and 150 < y < 850):
                    pencil = create_pencil(x, y, color, angle)
                    pencils.append(pencil)
                    break

    def toggle_canvas():
        if canvas_visible.get():
            canvas_frame.pack_forget()  
            close_button.config(text='Открыть')
            canvas_visible.set(False)
        else:
            canvas_frame.pack(side=BOTTOM, pady=(0, 20))  
            close_button.config(text='Закрыть')
            canvas_visible.set(True)

    def back_to_menu():
        root.destroy()
        main_root.deiconify()

    Button(top_frame, text='Перемешать', command=shuffle_pencils, **button_style).pack(side=LEFT, padx=5)
    Button(top_frame, text='Повернуть', command=rotate_pencils, **button_style).pack(side=LEFT, padx=5)
    close_button = Button(top_frame, text='Закрыть', command=toggle_canvas, **button_style)
    close_button.pack(side=LEFT, padx=5)
    Button(top_frame, text='В меню', command=back_to_menu, **button_style).pack(side=LEFT, padx=5)
    Button(top_frame, text='Выход', command=root.quit, **button_style).pack(side=RIGHT, padx=5)

    root.protocol("WM_DELETE_WINDOW", back_to_menu)
    shuffle_pencils()