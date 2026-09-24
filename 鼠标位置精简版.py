import pyautogui,time

while True:
    x, y = pyautogui.position()
    print(f"鼠标当前位置: X={x:4d}, Y={y:4d}", end="\r")
    time.sleep(0.1)