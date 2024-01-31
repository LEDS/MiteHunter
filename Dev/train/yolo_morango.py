#xyz
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'  # Address potential OpenMP library conflicts (optional)
from ultralytics import YOLO

# Load the model only when executed as the main script
if __name__ == '__main__':
    model = YOLO("yolov8s.yaml")  # Build a new model from scratch
    model.train(data="train-yolov8-custom-dataset-step-by-step-guide-master/local_env/config.yaml",
            name='train',
            close_mosaic=0,
            epochs=9999,
            batch=36,
            patience=100,
            imgsz=640,
            augment=True,
            cache=True,
            iou= 0.6,
            conf=0.3,
            optimize=True)
