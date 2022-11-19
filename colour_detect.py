import cv2
import numpy as np
from camera_detect import *

def main():
    colour_detect

def colour_detect():
    image_path = "/pi/recent_image.jpg"
    
    print("Colour Recognition Python")

    # Get image input
    img = cv2.imread(image_path)
    new_img = cv2.resize(img, (50, 50))
    height, width, _ = new_img.shape
    hsv_img = cv2.cvtColor(new_img, cv2.COLOR_BGR2HSV) # convert image from bgr 2 hsv

    array_store = []

    colour_dict = {'BLACK': [[180, 255, 30], [0, 0, 0]],
                'WHITE': [[180, 18, 255], [0, 0, 231]],
                'RED': [[180, 255, 255], [159, 50, 70]],
                'RED': [[9, 255, 255], [0, 50, 70]],
                'GREEN': [[89, 255, 255], [36, 50, 70]],
                'BLUE': [[128, 255, 255], [90, 50, 70]],
                'YELLOW': [[35, 255, 255], [25, 50, 70]],
                'PURPLE': [[158, 255, 255], [129, 50, 70]],
                'ORANGE': [[24, 255, 255], [10, 50, 70]],
                'GRAY': [[180, 18, 230], [0, 0, 40]]}

    for x in range(width):
        for y in range (height):
            hue = hsv_img[x,y][0]
            sat = hsv_img[x,y][1]
            value = hsv_img [x,y][2]
            
            for  colour in colour_dict:
                if ( (colour_dict[colour][1][0] < hue < colour_dict[colour][0][0]) and (colour_dict[colour][1][1] < sat < colour_dict[colour][0][1]) and (colour_dict[colour][1][2] < value < colour_dict[colour][0][2]) ):
                    array_store.append(colour)
                    break

    dictionary_test = {}

    for i in array_store:
        if i in dictionary_test:
            dictionary_test[i] += 1
        else:
            dictionary_test[i] = 1

    print(dictionary_test)

    final_colour = max(dictionary_test, key=dictionary_test.get)
    print("Maximum value: ",final_colour)
    
    return final_colour