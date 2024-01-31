from tkinter import *
from PIL import Image, ImageTk
import os
from ultralytics import YOLO


class AnnotationTool:
    def __init__(self, master, image_paths):
        self.master = master
        self.image_paths = image_paths
        self.current_index = 0
        self.start_x, self.start_y = None, None
        self.rectangles = []
        self.objects = []  # Lista de objetos com nome, número e cor
        self.zoom_factor = 1  # Initialize zoom factor here
        self.model = YOLO("C:/Users/carlo/OneDrive/backups/Documentos2/Notebooks/Estudo_Yolo/runs/detect/train13/weights/best.pt")

        self.canvas = Canvas(master, width=800, height=600)
        self.canvas.pack(fill='both', expand=True)  # Preenche e expande a janela

        self.load_image()
        self.canvas.bind("<ButtonPress-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)

        self.create_navigation_buttons()
        self.create_object_buttons()

    def add_zoom_buttons(self):
        zoom_in_button = Button(self.master, text="Zoom In", command=self.zoom_in)
        zoom_in_button.pack(side=LEFT)

        zoom_out_button = Button(self.master, text="Zoom Out", command=self.zoom_out)
        zoom_out_button.pack(side=LEFT)

    def zoom_in(self):
        self.zoom_factor *= 1.2  # Increase zoom factor
        self.resize_image()

    def zoom_out(self):
        self.zoom_factor /= 1.2  # Decrease zoom factor
        self.resize_image()

    def resize_image(self):
        new_width = int(self.img.width * self.zoom_factor)
        new_height = int(self.img.height * self.zoom_factor)
        resized_img = self.img.resize((new_width, new_height), Image.LANCZOS)

        self.tk_img = ImageTk.PhotoImage(resized_img)
        self.canvas.delete("all")  # Limpa todos os elementos do canvas
        self.canvas.create_image(0, 0, anchor="nw", image=self.tk_img)
        self.show_saved_rectangles()  # Atualiza para mostrar todas as anotações


    def load_image(self):
        self.canvas.delete("all")  # Limpa todos os elementos do canvas
        image_path = self.image_paths[self.current_index]
        self.img = Image.open(image_path)
        self.tk_img = ImageTk.PhotoImage(self.img)
        self.canvas.create_image(0, 0, anchor="nw", image=self.tk_img)

        self.load_annotations(image_path)  # Carrega as anotações correspondentes, se existirem

    def load_annotations(self, image_path):
        image_name = os.path.basename(image_path)
        txt_filename = f"{image_name}.txt"

        if os.path.exists(txt_filename):
            with open(txt_filename, 'r') as file:
                lines = file.readlines()

            self.rectangles = []
            for line in lines:
                values = line.strip().split()
                obj_index = int(values[0])
                x1, y1, x2, y2 = map(float, values[1:])
                self.rectangles.append((x1, y1, x2, y2, obj_index))

    def on_click(self, event):
        self.start_x, self.start_y = event.x, event.y

    def on_drag(self, event):
        if self.start_x and self.start_y:
            x, y = event.x, event.y
            print(x,y)
            if x < 0:
                x=0
            self.canvas.delete("rect")
            print(self.start_x, self.start_y, x, y)
            if ((self.start_x + self.start_y) < (x + y)):
                print(x, y, self.start_x, self.start_y)
                self.canvas.create_rectangle( x, y, self.start_x, self.start_y, outline='Black', tags="rect")
                print('if')
            else:
                print('Else')
                print(self.start_x, self.start_y, x, y)
                self.canvas.create_rectangle(self.start_x, self.start_y, x, y, outline='Black', tags="rect")

    def save_rectangle(self):
        if self.start_x and self.start_y and hasattr(self, 'selected_object'):
            x1, y1 = self.start_x, self.start_y
            x2, y2 = self.canvas.coords("rect")[2], self.canvas.coords("rect")[3]
            obj_index = self.selected_object["index"]  # Índice do objeto selecionado

            self.rectangles.append((x1, y1, x2, y2, obj_index))  # Adiciona as coordenadas e o índice do objeto
            
            image = Image.open(self.image_paths[self.current_index])
            modified_name = f"{os.path.basename(self.image_paths[self.current_index]).split('.')[0]}.jpg"
            image.save(modified_name)

            # Reload the modified image
            self.image_paths[self.current_index] = modified_name
            self.load_image()  # This will also reload the annotations from the .txt file

            # Salva as coordenadas em um arquivo de texto
            self.save_to_txt()

            self.show_saved_rectangles()  # Atualiza para mostrar todas as anotações


    def save_to_txt(self):
        print(self.image_paths[self.current_index].split('/')[-1].split('.')[0])
        txt_filename = f"{self.image_paths[self.current_index].split('/')[-1].split('.')[0]}.txt"
        with open(txt_filename, 'w') as file:
            for rect in self.rectangles:
                x_center = (rect[0] + rect[2]) / (2 * 640)
                y_center = (rect[1] + rect[3]) / (2 * 640)  # Calcula y_centro normalizado
                width = (rect[2] - rect[0]) / 640  # Calcula largura normalizada
                height = (rect[3] - rect[1]) / 640  # Calcula altura normalizada

                file.write(f"{rect[4]} {x_center} {y_center} {width} {height}\n")

    def clear_canvas(self):
        self.canvas.delete("rect")
        self.rectangles = []

    def create_navigation_buttons(self):
        prev_button = Button(self.master, text="Previous", command=self.prev_image)
        prev_button.pack(side=LEFT)

        next_button = Button(self.master, text="Next", command=self.next_image)
        next_button.pack(side=RIGHT)

    def create_object_buttons(self):
        object_frame = Frame(self.master)
        object_frame.pack()

        # Lista de objetos com nome, número e cor
        self.objects = [
            {"name": "Object 1", "index": 0, "color": "red"},
            {"name": "Object 2", "index": 1, "color": "blue"},
            {"name": "Object 2", "index": 2, "color": "purple"},
            # Adicione mais objetos conforme necessário
        ]

        for obj in self.objects:
            obj_button = Button(object_frame, text=obj["name"], bg=obj["color"], command=lambda o=obj: self.select_object(o))
            obj_button.pack(side=LEFT)

        add_obj_button = Button(object_frame, text="Add Object", command=self.add_object)
        add_obj_button.pack(side=LEFT)

    def select_object(self, obj):
        # Define o objeto selecionado para a anotação
        self.selected_object = obj

    def add_object(self):
        # Função para adicionar um novo objeto com nome e cor
        new_name = f"Object {len(self.objects) + 1}"
        new_color = self.get_random_color()  # Gera uma cor aleatória
        new_index = len(self.objects)
        new_obj = {"name": new_name, "index": new_index, "color": new_color}
        self.objects.append(new_obj)

        # Atualiza os botões de objetos
        obj_button = Button(self.master, text=new_name, bg=new_color, command=lambda o=new_obj: self.select_object(o))
        obj_button.pack(side=LEFT)

    def get_random_color(self):
        # Função para gerar uma cor hexadecimal aleatória
        import random
        return "#{:06x}".format(random.randint(0, 0xFFFFFF))

    def prev_image(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.load_image()

    def next_image(self):
        if self.current_index < len(self.image_paths) - 1:
            self.current_index += 1
            self.load_image()

    def show_saved_rectangles(self):
        self.canvas.delete("rectangles")
        for rect in self.rectangles:
            x1, y1, x2, y2, obj_index = rect
            obj = self.objects[obj_index]
            self.canvas.create_rectangle(x1*self.zoom_factor, y1*self.zoom_factor, x2*self.zoom_factor, y2*self.zoom_factor, outline=obj["color"], tags="rectangles")

def get_image_paths(directory):
    image_paths = [os.path.join(directory, file) for file in os.listdir(directory) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
    return image_paths

def main():
    directory = 'C:/Users/carlo/OneDrive/backups/Documentos2/Notebooks/Estudo_Yolo/Dev/icons/'  # Caminho especificado
    image_paths = get_image_paths(directory)

    root = Tk()
    root.title("LEDS Annotation Tool")
    app = AnnotationTool(root, image_paths)

    save_button = Button(root, text="Save Rectangle", command=app.save_rectangle)
    save_button.pack()

    clear_button = Button(root, text="Clear Canvas", command=app.clear_canvas)
    clear_button.pack()
    app.add_zoom_buttons()  # Add zoom buttons

    root.mainloop()

if __name__ == "__main__":
    main()
