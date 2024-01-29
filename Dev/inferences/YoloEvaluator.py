from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
from ultralytics import YOLO
import cv2
import threading
import json
from PIL import Image
import datetime
import time

model = YOLO('/home/carlos/Documentos/iniciacao_cientifica/Estudo_Yolo/runs/detect/train5_320e640/weights/best.pt')
def make_json_file(arquivo_file, novos_dados):
    """
    Cria ou atualiza um arquivo JSON com os dados especificados.

    Args:
        arquivo: Caminho do arquivo JSON.
        novos_dados: Lista de dicionários a serem adicionados ao arquivo JSON.

    Returns:
        None.
    """

    # Adicione os novos dados a uma lista
    data_existente = []  # Lista vazia para armazenar os dados existentes
    observer.join()
    try:
        found = False
        arquivo =  open(arquivo_file, 'r+')
        # Tenta carregar os dados existentes
        # Se houver um erro ao decodificar JSON (por exemplo, se o arquivo estiver vazio), inicia com um dicionário vazio
        data_existente_dict = json.load(arquivo)
        # Adicione os novos dados aos dados existentes
        for i in range(len(data_existente_dict)):#change for while
            if (novos_dados['imgOrig']) == (data_existente_dict[i]['imgOrig']):
                found = True
        if found == False:
            data_existente_dict.append(novos_dados)
            # Salva todos os dados
            with open("Seumorangudo.json", "w") as f:
                json.dump(data_existente_dict, f, indent=4)
            arquivo.close()
    except FileNotFoundError:
            # Se o arquivo não for encontrado, cria um novo arquivo com os dados existentes
            print("Arquivo não encontrado. Criando um novo arquivo com os dados existentes...")
            data_existente.append(novos_dados)
            with open(arquivo_file, 'w') as f:
                json.dump(data_existente, f, indent=4)



def get_image_info(image_path):
    """
    Recupera informações de uma imagem, incluindo dados EXIF e nome do arquivo.

    Args:
        image_path: Caminho da imagem.

    Returns:
        Um dicionário contendo as informações da imagem, incluindo:
            - data: Data da imagem (se disponível nos dados EXIF, no formato YYYY:MM:DD HH:MM:SS).
            - name: Nome do arquivo da imagem.
    """
    # Abra a imagem usando Pillow
    image = Image.open(image_path)

    stat = os.stat(image_path)

    creation_time = stat.st_ctime
    creation_date = datetime.datetime.fromtimestamp(creation_time)

    data = creation_date.strftime("%d-%m-%Y")

    path = os.path.abspath(image_path)

    name = os.path.basename(path)


    return {"data": data, "name": name}

class ImgProcessor(threading.Thread):
    def __init__(self, image_path):
        threading.Thread.__init__(self)
        self.image_path = image_path
        self.californicus = 0
        self.macropilis = 0
        self.rajado = 0

    def run(self):
        #print(f"Processando imagem: {self.image_path}")

        image = cv2.imread(self.image_path)
        image = cv2.resize(image, (640, 640))
        results = model(source=image,show_labels=False,show_conf=False,show_boxes=False)
        non_overlapping_boxes = []
        x1=0
        y1=0
        x2=0
        y2=0
        classes = []
        for box, conf, cls in zip(results[0].boxes.xyxy, results[0].boxes.conf, results[0].boxes.cls):
            x1, y1, x2, y2 = box.tolist()
            is_overlapping = False
            for existing_box in non_overlapping_boxes:
                existing_x1, existing_y1, existing_x2, existing_y2 = existing_box

                x_overlap = max(0, min(x2, existing_x2) - max(x1, existing_x1))
                y_overlap = max(0, min(y2, existing_y2) - max(y1, existing_y1))
                intersection_area = x_overlap * y_overlap
                union_area = (x2 - x1) * (y2 - y1) + (existing_x2 - existing_x1) * (existing_y2 - existing_y1) - intersection_area
                iou = intersection_area / union_area
                
                if iou > 0.70:#verify if iou metrics is more than X%
                    is_overlapping = False
                    break

            if not is_overlapping:
                non_overlapping_boxes.append(box)

                if cls == 0:
                    self.californicus += 1

                elif cls == 1:
                    self.macropilis += 1

                elif cls == 2:
                    self.rajado += 1

            classes.append((cls.item(),conf.item(),x1,y1,x2,y2))
        image_info = get_image_info(self.image_path)
        
        return {"californicus": self.californicus,
                "macropilis": self.macropilis,
                "rajado": self.rajado,
                "id":image_info['name'].split("_")[0],
                "imgOrig": image_info['name'],
                "imgProc": classes,
                "data": image_info['data']
                } #This is the paramethers from JSON

class MyHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.lock = threading.Lock()
    def process_image_in_thread(self, image_path, previous_folder):
        img_processor = ImgProcessor(image_path)
        with self.lock:
            data = img_processor.run()
            make_json_file("Seumorangudo.json", data)
        os.rename(image_path, os.path.join("C:/Users/carlo/OneDrive/backups/Documentos2/Notebooks/Estudo_Yolo/dataset/processadas/", os.path.basename(image_path)))


    def on_modified(self, event):
        if event.event_type == "modified":
            # wait x minutes
            time.sleep(5)

            for image_path in os.listdir("C:/Users/carlo/OneDrive/backups/Documentos2/Notebooks/Estudo_Yolo/dataset/images/"):
                full_image_path = "C:/Users/carlo/OneDrive/backups/Documentos2/Notebooks/Estudo_Yolo/dataset/images/" + image_path
                previous_folder = os.path.dirname(full_image_path)

                thread = threading.Thread(target=self.process_image_in_thread, args=(full_image_path, previous_folder))
                thread.start()



event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path='dataset/images', recursive=True)
observer.start()