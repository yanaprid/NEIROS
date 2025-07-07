#figures
from tkinter import *
import random
from math import radians, cos, sin

def fplay(main_root):
    root = Toplevel()
    root.geometry("1000x1000")
    root.title("ВРАЩАЮЩИЕСЯ ФИГУРЫ")
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

    Label(count_frame, text='Выберите количество фигур:', 
          font=('Arial', 16), bg='#F0E6FF', fg='#5A189A').pack()

    var = IntVar(value=0)
    colvo = [("5", 0), ("6", 1), ("7", 2)]

    for text, value in colvo:
        Radiobutton(count_frame, text=text, variable=var, value=value, 
                   font=('Arial', 14), bg='#F0E6FF', fg='#5A189A',
                   activebackground='#F0E6FF', selectcolor='#E0AAFF').pack(side=LEFT, padx=5)

    shape_types = ['rectangle', 'square', 'ellipse', 'circle', 'triangle']
    colors = ['red', 'green', 'blue', 'yellow', 'orange']
    shapes = []

    def paint(shape_type, x, y, color):
        if shape_type == 'rectangle':
            width, height = 350, 170
            shape_id = c.create_rectangle(x, y, x+width, y+height, fill=color, outline='black')
        elif shape_type == 'square':
            width = height = 250
            shape_id = c.create_rectangle(x, y, x+width, y+height, fill=color, outline='black')
        elif shape_type == 'ellipse':
            width, height = 270, 190
            shape_id = c.create_oval(x, y, x+width, y+height, fill=color, outline='black')
        elif shape_type == 'circle':
            width = height = 230
            shape_id = c.create_oval(x, y, x+width, y+height, fill=color, outline='black')
        elif shape_type == 'triangle':
            width, height = 250, 250
            points = [x, y+height, x+width/2, y, x+width, y+height]
            shape_id = c.create_polygon(points, fill=color, outline='black')
        return width, height, shape_id

    def rotate_shapes():
        for shape in shapes:
            shape_type, shape_id, x, y, width, height, angle = shape
            new_angle = (angle + 90) % 360
            shape[6] = new_angle
    
            center_x = x + width/2
            center_y = y + height/2
            rad = radians(new_angle)
    
            coords = c.coords(shape_id)
            points = [(coords[i], coords[i+1]) for i in range(0, len(coords), 2)]
    
            rotated_points = []
            for px, py in points:
                px -= center_x
                py -= center_y
                new_px = px * cos(rad) - py * sin(rad)
                new_py = px * sin(rad) + py * cos(rad)
                rotated_points.extend([new_px + center_x, new_py + center_y])
    
            c.coords(shape_id, *rotated_points)

    def shuffle_shapes():
        c.delete("all")
        shapes.clear()
        
        selected = var.get()
        num_shapes = [5, 6, 7][selected]
        
        all_combinations = [(shape, color) for shape in shape_types for color in colors]
        random.shuffle(all_combinations)
       
        
        selected_combinations = all_combinations[:num_shapes]
        
        canvas_width = 900
        canvas_height = 700
        margin = 50
        
        grid_cols = int(num_shapes**0.5) + 1
        grid_rows = (num_shapes + grid_cols - 1) // grid_cols
        cell_width = (canvas_width - 2*margin) / grid_cols
        cell_height = (canvas_height - 2*margin) / grid_rows
        
        for i, (shape_type, color) in enumerate(selected_combinations):
            if shape_type == 'rectangle':
                width, height = 250, 130
            elif shape_type == 'square':
                width = height = 200
            elif shape_type == 'ellipse':
                width, height = 220, 110
            elif shape_type == 'circle':
                width = height = 180
            elif shape_type == 'triangle':
                width, height = 200, 200
            
            col = i % grid_cols
            row = i // grid_cols
            
            x = margin + col * cell_width + cell_width/2 - width/2 + random.uniform(-cell_width/4, cell_width/4)
            y = margin + row * cell_height + cell_height/2 - height/2 + random.uniform(-cell_height/4, cell_height/4)
            
            x = max(margin, min(x, canvas_width - width - margin))
            y = max(margin, min(y, canvas_height - height - margin))
            
            width, height, shape_id = paint(shape_type, x, y, color)
            shapes.append([shape_type, shape_id, x, y, width, height, 0])

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

    Button(top_frame, text='Перемешать', command=shuffle_shapes, **button_style).pack(side=LEFT, padx=5)
    Button(top_frame, text='Повернуть', command=rotate_shapes, **button_style).pack(side=LEFT, padx=5)
    close_button = Button(top_frame, text='Закрыть', command=toggle_canvas, **button_style)
    close_button.pack(side=LEFT, padx=5)
    Button(top_frame, text='В меню', command=back_to_menu, **button_style).pack(side=LEFT, padx=5)
    Button(top_frame, text='Выход', command=root.quit, **button_style).pack(side=RIGHT, padx=5)

    root.protocol("WM_DELETE_WINDOW", back_to_menu)
    shuffle_shapes()