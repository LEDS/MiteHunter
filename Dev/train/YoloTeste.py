import cv2  
import os
import numpy as np

os.environ['KMP_DUPLICATE_LIB_OK']='True'

from ultralytics import YOLO

# Load the trained model
model = YOLO("C:/Users/carlo/OneDrive/backups/Documentos2/Notebooks/Estudo_Yolo/runs/detect/train5_320e640/weights/best.pt")

# Load the test image
image = cv2.imread("C:/Users/carlo/OneDrive/backups/Documentos2/Notebooks/Estudo_Yolo/dataset/images/20210331103347-Phytoseiulus_persimilis-94_7f76f177e1.jpg")

# Resize the image to the model's input size
image = cv2.resize(image, (640, 640))

# Run prediction
results = model(source=image)
color = (0, 255, 0) 
# Iterate through bounding boxes, checking for overlaps
non_overlapping_boxes = []
for box, conf, cls in zip(results[0].boxes.xyxy, results[0].boxes.conf, results[0].boxes.cls):
    x1, y1, x2, y2 = box.tolist()
    is_overlapping = False

    for existing_box in non_overlapping_boxes:
        existing_x1, existing_y1, existing_x2, existing_y2 = existing_box

        # Check for overlap condition (Intersection over Union, IoU)
        x_overlap = max(0, min(x2, existing_x2) - max(x1, existing_x1))
        y_overlap = max(0, min(y2, existing_y2) - max(y1, existing_y1))
        intersection_area = x_overlap * y_overlap
        union_area = (x2 - x1) * (y2 - y1) + (existing_x2 - existing_x1) * (existing_y2 - existing_y1) - intersection_area
        iou = intersection_area / union_area

        if iou > 0.70:  # Adjust threshold as needed
            is_overlapping = True
            break

    if not is_overlapping:
        non_overlapping_boxes.append(box)

        # Process non-overlapping box (draw, display text, etc.)
        if cls == 0:#amadurecimento
            color = (0,255,255)#BGR
        elif cls == 1:
            color = (0, 0, 255)#maduro
        elif cls == 2:
            color = (0, 255, 0)#verde
        cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), color, 1)
    # Converter a cor para o formato BGR
        color_bgr = tuple(reversed(color))

    # Definir a posição e o tamanho do texto
        text_position = (int(x1), int(y1) - 5)
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.5
        font_thickness = 1

        # Obter o tamanho do texto para determinar o tamanho do quadrado
        conf = int(conf*100)
        text_size = cv2.getTextSize(f"{conf:.0f}", font, font_scale, font_thickness)[0]
        square_padding = 5
        square_start = (text_position[0] - square_padding, text_position[1] - text_size[1] - square_padding)
        square_end = (text_position[0] + text_size[0] + square_padding, text_position[1] + square_padding)

        # Adicionar um quadrado colorido atrás do número
        cv2.rectangle(image, square_start, square_end, color, -1)  # -1 preenche o retângulo

        # Colocar o texto na imagem após desenhar o retângulo colorido
        cv2.putText(image, f"{conf:.0f}", text_position, font, font_scale, color_bgr*0, font_thickness)

# Display the image
cv2.imshow("X", image)
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()
