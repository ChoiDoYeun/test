import subprocess
import torch
import cv2
import numpy as np
from PIL import Image
from pyzbar.pyzbar import decode

# 감지된 객체 크롭하고 저장하는 함수
def crop_object(results, img_pil, output_path):
    if len(results.xyxy[0]) > 0:  # 객체가 감지된 경우
        x_min, y_min, x_max, y_max = results.xyxy[0][0][:4].cpu().numpy().astype(int)
        cropped_img = img_pil.crop((x_min, y_min, x_max, y_max))
        cropped_img.save(output_path)

# 이미지 리사이즈 함수
def resize_image(input_path, output_path, size=(450, 450)):
    image = Image.open(input_path)
    resized_image = image.resize(size)
    resized_image.save(output_path)

# QR 코드 읽는 함수
def read_qr_code(image_path):
    img = Image.open(image_path)
    decoded_objects = decode(img)
    return decoded_objects[0].data.decode() if decoded_objects else ""

def capture_image(output_path):
    # 경로 설정
    base_path = "/home/dodo/test/"
    model_path = base_path + 'best.pt'
    
    # 저장된 모델 로드
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, force_reload=True)
    torch.save(model.state_dict(), "local_model_path.pt")
    model.load_state_dict(torch.load("local_model_path.pt"))
    
    # 카메라 설정
    cap = cv2.VideoCapture(0)  # 0은 기본 카메라
    
    try:
        while True:
            # 카메라로부터 이미지 읽기
            ret, frame = cap.read()
            if not ret:
                break
            
            # OpenCV 이미지를 PIL 이미지로 변환
            img_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    
            # 모델을 사용하여 이미지에서 객체 감지
            results = model(img_pil)
    
            # 감지된 객체 처리
            cropped_img_path = base_path + 'cropped_test.png'
            output_path = base_path + 'resize_test.png'
            crop_object(results, img_pil, cropped_img_path)
            resize_image(cropped_img_path, output_path)

            qr_code = read_qr_code(output_path)
            print("QR Code:", qr_code)

            if qr_code:
                break  # qr_code가 생성되면 반복문 종료

    finally:
        cap.release()
        cv2.destroyAllWindows()

    return qr_code
