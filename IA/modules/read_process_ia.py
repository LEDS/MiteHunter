from sahi.predict import predict, get_sliced_prediction
from .sample_elements import SampleTableElements
from sahi import AutoDetectionModel
from dataclasses import dataclass
from .jsons_folder_read import *
from sahi.predict import predict
from __init__ import JSONS_PATH
from ultralytics import YOLO
from types import NoneType
from datetime import date
from pathlib import Path
from PIL import Image
import numpy as np
import shutil
import json
import cv2
import os


@dataclass
class Counted:
    rajado: int
    macropilis: int
    californicus: int


@dataclass
class ProcessedImage:
    folder_name: str
    image: Path
    counts: Counted


@dataclass
class ErrorImage:
    folder_name: str
    image: Path
    exception: str


class OutputCounter:
    def __init__(self, *, model: Path, input_images_path: Path, processed_images_path: Path,
                bouding_box_processed_images_path: Path, error_images_path: Path, yolo_predict_path: Path):
        self.model_path: Path = model
        self.input_images_path: Path = input_images_path
        self.processed_images_path: Path = processed_images_path
        self.bouding_box_processed_images_path = bouding_box_processed_images_path
        self.error_images_path: Path = error_images_path
        self.yolo_predict_path = yolo_predict_path

        self.processed_images: dict = {}
        self.error_images: dict = {}


    @staticmethod
    def move_file(path1: Path, path2: Path):
        shutil.move(str(path1), str(path2))

    @staticmethod
    def remove_folder(folder: Path, folder_name:str):
        folder_content = os.listdir(folder)
        if len(folder_content) == 0:
            os.rmdir(folder)
            sample_table_elements = SampleTableElements()
            sample_table_elements.count_elements(Path(folder_name))
            check_exists_files_folder(sample_table_elements.file_count_dict)

    @staticmethod
    def write_json(json_file_path: Path, json_data: Path):
        # Verifica se o caminho do arquivo existe
        if not json_file_path.exists():
            # Se não existir, cria o diretório "amostras" e o arquivo "a.json"
            json_file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(json_file_path, "w") as json_file:
                json.dump([], json_file)

        # Abre o arquivo JSON e carrega o conteúdo em uma lista
        with open(json_file_path, "r") as json_file:
            data_list = json.load(json_file)

        # Adiciona o dicionário à lista existente
        data_list.append(json_data)

        # Escreve a lista atualizada no arquivo
        with open(json_file_path, "w") as json_file:
            json.dump(data_list, json_file)

    def count_image(self, img_path: Path, bouding_box_img_path: Path, original_image_name:str) -> Counted:
        counted = Counted(
            rajado = 0,
            macropilis = 0,
            californicus = 0
        )

        # Detection model initialization
        detection_model = AutoDetectionModel.from_pretrained(
            model_type="yolov8",
            model_path=self.model_path,
            confidence_threshold=0.3,
            device="cuda:0",
        )

        # Making predictions using SAHI to detect smaller objects
        result = get_sliced_prediction(
            image=Image.open(img_path),
            detection_model=detection_model,
            slice_height=640,
            slice_width=640,
            overlap_height_ratio=0.2,
            overlap_width_ratio=0.2,
            postprocess_class_agnostic=True,
        )

        names = {
            "Rajado": "R",
            "Californicus": "C",
            "Macropilis": "M"
        }

        for obj in result.object_prediction_list:
            obj.category.name = names[obj.category.name]

        # Exporting image with bounding boxes
        result.export_visuals(export_dir=bouding_box_img_path, file_name=original_image_name, text_size=1.25, rect_th=3)

        # Accessing the list of predicted objects
        object_prediction_list = result.object_prediction_list

        # Using a for to access the id of each category/bounding box
        for i in object_prediction_list:
            _class = i.category.id
            match _class:
                case 0: counted.californicus += 1
                case 1: counted.macropilis += 1
                case 2: counted.rajado += 1

        return counted


    def count(self) -> NoneType:
        folders: list[Path] = [item for item in self.input_images_path.iterdir() if item.is_dir()]

        for folder in folders:
            # Descobre o usuario pelo nome da pasta
            folder_name: str = str(folder.name)
            list_separate_folder_name = folder_name.split("_")
            cultivo_id: int = list_separate_folder_name[0]
            sample_date: date = f"{list_separate_folder_name[1][:4]}-{list_separate_folder_name[1][4:6]}-{list_separate_folder_name[1][6:8]}"
            folder_name_processed_images_path = self.processed_images_path / folder_name
            bouding_box_processed_images_path = self.bouding_box_processed_images_path / folder_name
            folder_name_error_images_path = self.error_images_path / folder_name
            
            # Para cada usuário, roda o modelo em cada arquivo
            images: list[Path] = [item for item in folder.iterdir() if item.is_file()]
            for img_path in images:
                try:
                    processed_img_path = folder_name_processed_images_path / img_path.name
                    bb_processed_img_path = folder_name_processed_images_path
                    
                    if not folder_name_processed_images_path.exists():
                        folder_name_processed_images_path.mkdir()
                    
                    image_name_split = (img_path.name).split(".")
                    original_image_name = image_name_split[0] + "_BB"
                    
                    counts = self.count_image(img_path, bb_processed_img_path, original_image_name)
                    
                    self.processed_images = {
                        "cultivo_id": int(cultivo_id),
                        "imgOrig": str(processed_img_path),
                        "imgProc": f"{str(bouding_box_processed_images_path)}\\{original_image_name}",
                        "data_Amos":sample_date,
                        "rajado": counts.rajado,
                        "macropilis": counts.macropilis,
                        "californicus": counts.californicus
                    }

                    self.write_json(Path(f'{JSONS_PATH}/{folder_name}.json'), self.processed_images)
                    
                    self.move_file(img_path, processed_img_path)
                    self.processed_images.clear()
                    self.remove_folder(folder, folder_name)
                                    
                except Exception as e:
                    print(e)