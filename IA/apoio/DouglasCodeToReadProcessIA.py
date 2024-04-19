from dataclasses import dataclass
from ultralytics import YOLO
from types import NoneType
from pathlib import Path
import numpy as np
import shutil
import cv2
import os


@dataclass
class Counted:
    rajado: int
    macropilis: int
    californicus: int


@dataclass
class ProcessedImage:
    folderName: str
    image: Path
    counts: Counted


@dataclass
class ErrorImage:
    folderName: str
    image: Path
    exception: str


@dataclass
class DataToInsertIntoSampleTable:
    final_classification: str
    spider_mite_avaragde: float
    sugested_action: str
    leaf_total: int  #TODO alter this name to "foliolo_total" in english
    moreThan_nine: float
    lessThanOrEqual_nine_and_moreThanOrEqual_five: float
    lessThan_five_and_moreThan_zero: float
    leaf_without_spiderMite_and_predeatorMite: float
    leaf_with_spiderMite_and_predatorMite: float
    leaf_with_predatorMite_and_without_spiderMite: float


class OutputCounter:
    def __init__(self, *, model: YOLO, input_images_path: Path, processed_images_path: Path,
                bouding_box_processed_images_path: Path, error_images_path: Path, yolo_predict_path: Path):
        self.model: YOLO = model
        self.input_images_path: Path = input_images_path
        self.processed_images_path: Path = processed_images_path
        self.bouding_box_processed_images_path = bouding_box_processed_images_path
        self.error_images_path: Path = error_images_path
        self.yolo_predict_path = yolo_predict_path

        self.processed_images: list[{dict}] = []
        self.error_images: list[ErrorImage] = []


    @staticmethod
    def move_file(path1: Path, path2: Path):
        shutil.move(str(path1), str(path2))

    @staticmethod
    def remove_folder(folder: Path):
        folder_content = os.listdir(folder)
        if len(folder_content) == 0:
            os.rmdir(folder)


    def count_image(self, img_path: Path, bouding_box_img_path: Path) -> Counted:
        counted = Counted(
            rajado = 0,
            macropilis = 0,
            californicus = 0
        )

        cv2_image: np.ndarray = cv2.imread(str(img_path))
        cv2_image_resized: np.ndarray = cv2.resize(cv2_image, (640, 640))

        results = self.model(
            source = cv2_image_resized,
            save = False
        )

        #self.move_file(self.yolo_predict_path / "image0.jpg", bouding_box_img_path)
        #self.yolo_predict_path.rmdir()

        for _class in results[0].boxes.cls:
            match _class:
                case 0: counted.californicus += 1
                case 1: counted.macropilis += 1
                case 2: counted.rajado += 1

        return counted


    def count(self) -> NoneType:
        folders: list[Path] = [item for item in self.input_images_path.iterdir() if item.is_dir()]

        for folder in folders:
            # Descobre o usuario pelo nome da pasta
            folderName: str = str(folder.name)
            folderName_processed_images_path = self.processed_images_path / folderName
            bouding_box_processed_images_path = self.bouding_box_processed_images_path / folderName
            folderName_error_images_path = self.error_images_path / folderName

            # Para cada usuário, roda o modelo em cada arquivo
            images: list[Path] = [item for item in folder.iterdir() if item.is_file()]
            for img_path in images:
                print (img_path)
                try:
                    processed_img_path = folderName_processed_images_path / img_path.name
                    bb_processed_img_path = bouding_box_processed_images_path / img_path.name
                    if not folderName_processed_images_path.exists():
                        folderName_processed_images_path.mkdir()
                    
                    counts = self.count_image(img_path, bb_processed_img_path)
                    self.move_file(img_path, processed_img_path)
                    self.remove_folder(folder)
                    
                    processed_img_path.__str__()

                    self.processed_images.append(
                        ProcessedImage(
                            folderName = folderName,
                            image = str(processed_img_path),
                            counts = counts
                        )
                    )
                except Exception as e:
                    error_img_path = folderName_error_images_path / img_path.name

                    if not folderName_error_images_path.exists():
                        folderName_error_images_path.mkdir()
                    
                    self.move_file(img_path, error_img_path)
                    self.remove_folder(folder)
                    
                    self.error_images.append(
                        ErrorImage(
                            folderName = folderName,
                            image = error_img_path,
                            exception = str(e)
                        )
                    )