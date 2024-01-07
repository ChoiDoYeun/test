import subprocess

# 사진 파일의 경로를 설정합니다.
image_path = "image.jpg"

# libcamera-still 명령을 구성합니다.
command = f"libcamera-still -o {image_path}"

# 명령을 실행합니다.
subprocess.run(command, shell=True)

print(f"사진이 {image_path}에 저장되었습니다.")
