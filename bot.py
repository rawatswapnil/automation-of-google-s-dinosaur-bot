from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class Coordinates():
    replayBtn = (340, 390)
    dinosaur = (140, 410)

def restartGame():
    pyautogui.click(Coordinates.replayBtn)
    pyautogui.keyDown('down')

def pressSpace():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    print("Jump")
    time.sleep(0.18)
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')

def imageGrab():
    box = (Coordinates.dinosaur[0]+60,Coordinates.dinosaur[1],
           Coordinates.dinosaur[0]+150,Coordinates.dinosaur[1]+5)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())
    return a.sum()

def main():
    restartGame()
    while True:
        if(imageGrab()!=697):
            pressSpace()
            time.sleep(0.1)

main()
