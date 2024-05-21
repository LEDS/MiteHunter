from .modules.read_process_ia import OutputCounter
from .__init__ import INPUT_IMAGES_PATH, MODEL_PATH, PROCESSED_IMAGES_PATH, ERROR_IMAGES_PATH, BOUDING_BOX_PROCESSED_IMAGES_PATH, YOLO_PREDICT_PATH
from ultralytics import YOLO
from pathlib import Path
import supervision as sv
import numpy as np

model = YOLO(model = Path(MODEL_PATH))

def callback(image: np.ndarray) -> sv.Detections:
    result = model(image)[0]
    return sv.Detections.from_ultralytics(result)


def seila(image, sliced_detections, labels):
    slicer = sv.InferenceSlicer(callback=callback)
    detections = slicer(image=image)

    prediction_num = len(sliced_detections.xyxy)

    box_annotator = sv.BoxAnnotator()

    annotated_frame = box_annotator.annotate(
        scene=image.copy(),
        detections=detections,
        labels=labels
    )

    sv.plot_image(image=annotated_frame, size=(16, 16))



def executar(counter):
    counter.count()

def main(model_path: Path, input_images_path: Path, processed_images_path: Path, error_images_path: Path,
            bouding_box_processed_images_path: Path, yolo_predict_path: Path):
    print("CRIANDO MODELO")
    print("CRIANDO CONTADOR")
    
    counter = OutputCounter(
        model = model,
        input_images_path = input_images_path,
        processed_images_path = processed_images_path,
        bouding_box_processed_images_path = bouding_box_processed_images_path,
        error_images_path = error_images_path,
        yolo_predict_path = yolo_predict_path,
        callback=callback,
        seila=seila
    )
    print("EXECUTNDO MODELOS")

    executar(counter)

def run_ia():
    main(*[Path(i) for i in (MODEL_PATH, INPUT_IMAGES_PATH, PROCESSED_IMAGES_PATH, ERROR_IMAGES_PATH, BOUDING_BOX_PROCESSED_IMAGES_PATH, YOLO_PREDICT_PATH)])


if __name__ == "__main__":
    run_ia()