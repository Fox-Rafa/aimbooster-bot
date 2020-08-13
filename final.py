from PIL import Image
from PIL import ImageGrab
import pyautogui

target_colour = (255, 218, 192, 255)

target_window = [0, 0, 0, 0]
print("Put your mouse on the top left corner of the aimbooster target window and send any key in the terminal:")
a = input()
target_window[0], target_window[1] = pyautogui.position()[0], pyautogui.position()[1]
x0, y0 = target_window[0], target_window[1]

print("Put your mouse on the bottom left corner of the aimbooster target window and send any key in the terminal:")
a = input()
target_window[2], target_window[3] = pyautogui.position()[0], pyautogui.position()[1]

print(target_window)


while True:
    #Takes a screenshot of the screen
    im = ImageGrab.grab(bbox=target_window)

    #Loads it as an array of pixels
    pixels = im.load()
    width, height = im.size
    #Runs through the array looking for a orange pixel
    for x in range(width):
        for y in range(height):
            #Gets the colour of the current pixel
            pixel_colour = pixels[x,y]

            #Checks if the colour of the pixel is the same as the colour of the target
            if pixel_colour == target_colour:
                #Moves the mouse to the position of the target and clicks it
                pyautogui.click(x+x0, y+y0)
                break
        else:
            continue
        break
