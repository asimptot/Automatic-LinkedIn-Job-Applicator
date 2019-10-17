from selenium import webdriver
import pyautogui as pg
import time

def apply():
    pg.click(332, 748) #chrome
    time.sleep(5)

    for i in range(0, 20, 2):
        pg.click(87, 54)  # refresh
        time.sleep(15)
        for j in range(29+i):
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

        pg.click(918, 169) #close
        time.sleep(3)

apply()



