#引入库
import pyautogui as pa
import time

#防崩溃
pa.useImageNotFoundException(False)

#侦测开始
print("侦测5秒后开始...")
time.sleep(5)

def send_qq_notify(msg):
    pa.hotkey('ctrl', 'alt', 'z')
    time.sleep(2)
    pa.typewrite(msg)
    time.sleep(2)
    pa.press('enter')
    time.sleep(2)
    print("QQ消息发送完毕！")

#侦测新服是否开启
while True:
    try:
#打开服务器列表
        pa.moveTo(x=800,y=650)
        pa.click()
        time.sleep(3)
#打开最新服务器列表
        pa.moveTo(x=610,y=290)
        pa.click()
        time.sleep(3)
#发现新服
        search_region = (840, 210, 30, 80)
        st = list(pa.locateAllOnScreen('xin.png', confidence=0.7, region=search_region))
        if len(st) >= 2:
           send_qq_notify("1")
           time.sleep(5)
           pa.hotkey('alt', 'tab')
           time.sleep(5)
           pa.moveTo(x=885, y=190)
           pa.click()
           time.sleep(3600)
#未发现新服
        elif len(st) == 1:
           print("暂无新服，关闭列表，20秒后进行下一次侦测。")
           pa.moveTo(x=885,y=190)
           pa.click()
           time.sleep(20)
        else:
           print("未识别到图像，20秒后重试")
           pa.moveTo(x=885,y=190)
           pa.click()
           time.sleep(20)

    except Exception as e:
        print(f"发生异常: {e}，20秒后重试...")
        pa.moveTo(x=885, y=190)
        pa.click()
        time.sleep(20)
