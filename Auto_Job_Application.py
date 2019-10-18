from selenium import webdriver
import pyautogui as pg
import time

def open_chrome_in_toolbar():
    pg.click(330, 1048)  # chrome
    time.sleep(5)

def refresh():
    pg.click(129, 77)  # refresh
    time.sleep(15)

def close():
    pg.click(1277, 241)  # close
    time.sleep(3)

def apply():

    open_chrome_in_toolbar()
    refresh()

    for i in range(0, 25, 2):
        for j in range(28+i):
            pg.press('tab')
        pg.press('enter')

        for m in range(7):
            pg.press('tab')
        time.sleep(2)

        pg.press('enter') #right side
        time.sleep(3)

        for n in range(9):
            pg.press('tab')
        time.sleep(2)

        pg.press('enter') #apply
        time.sleep(2)

        close()

apply()



