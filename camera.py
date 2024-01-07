import cv2

def capture_image():
    # 카메라 캡처 객체 생성
    cap = cv2.VideoCapture(0)

    # 카메라로부터 사진 한 장 캡처
    ret, frame = cap.read()

    # 캡처가 성공했다면
    if ret:
        # 이미지 저장
        cv2.imwrite('captured_image.jpg', frame)
        print("사진이 저장되었습니다.")
    else:
        print("사진 캡처에 실패했습니다.")

    # 카메라 장치 해제
    cap.release()

capture_image()
