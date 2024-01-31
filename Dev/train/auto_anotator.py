import ultralytics
import torch
from ultralytics.yolo.data.annotator import auto_annotate
from ultralytics import SAM
# sam_l.pt and sam_b.pt

model = SAM('C:/Users/carlo/OneDrive/backups/Documentos2/Notebooks/Estudo_Yolo/runs/detect/train13/weights/best.pt')

auto_annotate(data="Dev/icons/Pimenta-Rosa.jpg", det_model="C:/Users/carlo/OneDrive/backups/Documentos2/Notebooks/Estudo_Yolo/runs/detect/train13/weights/best.pt", sam_model='sam_b.pt')
