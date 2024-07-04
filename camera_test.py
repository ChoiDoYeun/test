import torch
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from pyzbar.pyzbar import decode

# 경로
base_path = "/home/dodo/test/"
img_path = base_path + 'full_frame.png'
output_path = base_path + 'resize_test.png'
cropped_img_path = base_path + 'cropped_test.png'

# 저장된 모델 로드 및 재저장하여 git에서 클론하지않도록함
model_path = base_path + 'best.pt'
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, force_reload=True)
torch.save(model.state_dict(), "local_model_path.pt")
model.load_state_dict(torch.load("local_model_path.pt"))

# 감지된 객체 크롭 하여 저장
def crop_object(results, img_path, output_path):
    if len(results.xyxy[0]) > 0:  # If an object is detected
        x_min, y_min, x_max, y_max = results.xyxy[0][0][:4].cpu().numpy().astype(int)
        img = Image.open(img_path)
        cropped_img = img.crop((x_min, y_min, x_max, y_max))
        cropped_img.save(output_path)

# 크롭된 이미지 리사이즈
def resize_image(input_path, output_path, size=(450, 450)):
    image = Image.open(input_path)
    resized_image = image.resize(size)
    resized_image.save(output_path)

# qrcode decode
def read_qr_code(image_path):
    img = Image.open(image_path)
    decoded_objects = decode(img)
    return decoded_objects[0].data.decode() if decoded_objects else ""

for i in range(1,5):
  results = model(img_path)
  crop_object(results, img_path, cropped_img_path)
  resize_image(cropped_img_path, output_path)

  print(read_qr_code(output_path))
