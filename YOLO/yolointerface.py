from ultralytics import YOLO

model = YOLO("yolo26n.pt")

results = model("YOLO/magic_cards/cat.jpg")
