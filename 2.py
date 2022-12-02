from pynput import mouse
from PIL import ImageGrab
import time
 
def on_click(x, y, button, pressed): # pynput 마우스 클릭 이벤트
    btn = button.name

    if btn == 'left': 

        if pressed:
            a = time.strftime("%F-%H-%M-%S", time.localtime()) # 현재 시간 구함
            #a = "%04d-%02d-%02d_%02d시%02d분%02d초" %(n.tm_year, n.tm_mon, n.tm_mday, n.tm_hour, n.tm_min, n.tm_sec) # 현재시간 구함
            i = ImageGrab.grab()  # 스크린샷
            file = "{} {}".format(a, '.png') # 현재시간을 파일명으로
            i.save(file) # 저장


with mouse.Listener(on_click = on_click)as Listener:
	Listener.join()
