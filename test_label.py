import cv2

img = cv2.imread('0_0_92_26.jpg')

rows, cols, ch = img.shape

print('true width= ',cols,'true_height= ',rows)

x = 858
y = 376
height = cols
width = rows

xC = x/width
yC = y/height

print('xC= ',xC,'yC= ',yC)

