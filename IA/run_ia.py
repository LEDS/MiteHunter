from .modules.read_process_ia import OutputCounter
from .__init__ import INPUT_IMAGES_PATH, MODEL_PATH, PROCESSED_IMAGES_PATH, ERROR_IMAGES_PATH, BOUDING_BOX_PROCESSED_IMAGES_PATH, YOLO_PREDICT_PATH
from ultralytics import YOLO
from pathlib import Path

def executar(counter):
    counter.count()

def main(model_path: Path, input_images_path: Path, processed_images_path: Path, error_images_path: Path,
            bouding_box_processed_images_path: Path, yolo_predict_path: Path):
    print("CRIANDO MODELO")
    model = YOLO(model = model_path)
    print("CRIANDO CONTADOR")
    
    counter = OutputCounter(
        model = model,
        input_images_path = input_images_path,
        processed_images_path = processed_images_path,
        bouding_box_processed_images_path = bouding_box_processed_images_path,
        error_images_path = error_images_path,
        yolo_predict_path = yolo_predict_path
    )
    print("EXECUTNDO MODELOS")

    executar(counter)

def run_ia():
    main(*[Path(i) for i in (MODEL_PATH, INPUT_IMAGES_PATH, PROCESSED_IMAGES_PATH, ERROR_IMAGES_PATH, BOUDING_BOX_PROCESSED_IMAGES_PATH, YOLO_PREDICT_PATH)])


if __name__ == "__main__":
    run_ia()