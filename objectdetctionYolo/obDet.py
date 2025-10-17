from ultralytics import YOLO

# Load a pretrained Yolov8n Model
model = YOLO('yolov8n.pt')

# Run inference on the source
results = model(source="gymnasts.mp4", show=True, conf=0.4, save=True) # generator of 