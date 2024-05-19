import sys
import torch
from PIL import Image
import numpy as np
from pyzbar.pyzbar import decode

# YOLOv5 모듈 경로 추가
yolov5_path = "/home/dodo/yolov5"
if yolov5_path not in sys.path:
    sys.path.append(yolov5_path)

from models.experimental import attempt_load
from utils.general import non_max_suppression
from utils.torch_utils import select_device
from utils.plots import save_one_box

# 경로
base_path = "/home/dodo/test/"
img_path = base_path + 'captured_car.jpg'
output_path = base_path + 'resize_test.png'
cropped_img_path = base_path + 'cropped_test.png'
model_path = base_path + 'best.pt'

# 저장된 모델 로드
device = select_device('cpu')  # 'cuda' for GPU, 'cpu' for CPU
model = attempt_load(model_path, map_location=device)  # load FP32 model

# 감지된 객체 크롭하여 저장
def crop_object(results, img_path, output_path):
    if results is not None and len(results) > 0:  # If an object is detected
        for *box, conf, cls in results:  # Iterate through detected objects
            img = Image.open(img_path)
            save_one_box(box, img, file=output_path, BGR=True)

# 크롭된 이미지 리사이즈
def resize_image(input_path, output_path, size=(450, 450)):
    image = Image.open(input_path)
    resized_image = image.resize(size)
    resized_image.save(output_path)

# QR 코드 디코드
def read_qr_code(image_path):
    img = Image.open(image_path)
    decoded_objects = decode(img)
    return decoded_objects[0].data.decode() if decoded_objects else ""

# 이미지 로드 및 전처리
img = Image.open(img_path)
img = np.array(img)
img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB, to 3x416x416
img = np.ascontiguousarray(img)

# 모델 추론
img_tensor = torch.from_numpy(img).to(device)
img_tensor = img_tensor.float()  # uint8 to fp32
img_tensor /= 255.0  # 0 - 255 to 0.0 - 1.0
if img_tensor.ndimension() == 3:
    img_tensor = img_tensor.unsqueeze(0)

for i in range(1, 5):
    with torch.no_grad():
        pred = model(img_tensor, augment=False)[0]
        pred = non_max_suppression(pred, 0.25, 0.45, agnostic=False)
        results = pred if len(pred) > 0 else []

    crop_object(results, img_path, cropped_img_path)
    resize_image(cropped_img_path, output_path)

    qr_code_data = read_qr_code(output_path)
    print(qr_code_data)
