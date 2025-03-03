import pyautogui as pg
import time
print("program will run after 5 second")
time.sleep(5)
print('program will start in 5 seconds')
for i in range(50):
    # pg.write("I love you ❤️❤️❤️")
    pg.write('Yo')
    time.sleep(0.00000001)
    pg.press("Enter")
    