# MagicReach
A project to help magic players play with physical cards online

installs:
ultralytics
easyocr
scryfall


utilities:
ffmpeg - turning video in to frames for training
|| ffmpeg -i horizontalgameplay.mp4 -vf fps=1 dataset/raw/frame_%04d.jpg
|| generated 412 frames

labled frames manually
trained a yolo8 model on those lables for 100 epochs, finnish time 0.58
used the trained model to predict lables for the unlabled frames (338 frames)
corrected most frames by hand then trained the yolo8 model for 50 epochs on the compleate set of 412 frames with 86 validation items.

trianing cli:
yolo detect train data=dataset\data.yaml model=yolov8n.pt imgsz=512 epochs=20

prediction:
yolo detect predict model=runs\detect\train\weights\best.pt source=dataset\valid\images save=True conf=0.5 save_txt=True save_conf=False
