from ultralytics import YOLO

# Load a pretrained Yolov8n Model
model = YOLO('yolov8n.pt')

# Run inference on the source
results = model(source=0, show=True, conf=0.4, save=True) # generator of 