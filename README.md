# MagicReach
A project to help magic players play with physical cards online

installs:
ultralytics
easyocr


utilities:
ffmpeg - turning video in to frames for training
|| ffmpeg -i horizontalgameplay.mp4 -vf fps=1 dataset/raw/frame_%04d.jpg
|| generated 412 frames
