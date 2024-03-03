# toggle_mode.py
import threading
from qr_processor import process_qr_code_input,process_qr_code_output, StopThreadException

global qr_thread
qr_thread = None

def input_on(warehouse):
    global qr_thread
    # input용 qr코드 read를 위한 서보모터 동작 추가해야함
    qr_thread = threading.Thread(target=process_qr_code_input, args=(warehouse,))
    qr_thread.start()
    
def input_off():
    global qr_thread
    if qr_thread:
        qr_thread.raise_exception(StopThreadException)  # 예외를 발생시킵니다.
        qr_thread.join()  # 스레드가 종료될 때까지 기다립니다.
        
def output_on(warehouse):
    global qr_thread
    # output용 qr코드 read를 위한 서보모터 동작 추가해야함
    qr_thread = threading.Thread(target=process_qr_code_output, args=(warehouse,))
    qr_thread.start()
    
def output_off():
    global qr_thread
    if qr_thread:
        qr_thread.raise_exception(StopThreadException)  # 예외를 발생시킵니다.
        qr_thread.join()  # 스레드가 종료될 때까지 기다립니다.

# 스레드 객체에 예외를 발생시키는 메서드 추가
def raise_exception(self, exc):
    import ctypes
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(self.ident), ctypes.py_object(exc))
    if res > 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(self.ident, 0)
        raise SystemError("PyThreadState_SetAsyncExc failed")

threading.Thread.raise_exception = raise_exception