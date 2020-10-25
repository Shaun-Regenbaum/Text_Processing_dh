import cv2
from PIL import Image, ImageFont, ImageDraw  
import pytesseract
import numpy as np
import json


def new_section(x1,y1, x2, y2):
    if 

pytesseract.pytesseract.tesseract_cmd = 'A:\\Tesseract\\tesseract.exe'
img = cv2.imread('page_1.jpg')

heightImg, widthImg, channels  = img.shape

img2 = np.zeros((int(heightImg), int(widthImg), 3), np.uint8)
img2[:] = (255,255,255)

img_pil = Image.fromarray(img2)
draw = ImageDraw.Draw(img_pil)
font = ImageFont.truetype(r'C:\\Windows\\Fonts\\arial.ttf', size=10)
data = {}
boxes = pytesseract.image_to_boxes(img, lang='heb')
i = 0
for b in boxes.splitlines():
    b = b.split(' ')
    print(b)
    data[i] = []
    data[i].append({
        'x' : int(b[1]),
        'y' : int(b[2]),
        'width' : int(b[3]),
        'height' : int(b[4])
    })
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x, heightImg - y), (w,heightImg - h), (0, 0, 255), 1)
    i = i + 1
    draw.text((x, heightImg -y), str(i), fill='black', font=font, align="center") 


img2 = np.array(img_pil)
resize = cv2.resize(img, dsize=(int(widthImg*0.3), int(heightImg*0.3)), interpolation=cv2.INTER_AREA)
# cv2.imshow('Result', img2)
# cv2.waitKey(0)
cv2.imwrite("boxed_output.png", img)
cv2.imwrite("ordered.png", img2)



with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
