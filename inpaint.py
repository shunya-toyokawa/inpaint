import numpy as np
import cv2


# 画像を読む
img = cv2.imread('origin.png')
mask = cv2.imread('mask_origin.png',0)

# サイズ変更
#img = cv2.resize(img, (200, 200))
#mask = cv2.resize(mask, (200, 200))

# Inpainting
dst11 = cv2.inpaint(img,mask,0,cv2.INPAINT_TELEA)
dst12 = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)
dst13 = cv2.inpaint(img,mask,10,cv2.INPAINT_TELEA)
dst21 = cv2.inpaint(img,mask,0,cv2.INPAINT_NS)
dst22 = cv2.inpaint(img,mask,3,cv2.INPAINT_NS)
dst23 = cv2.inpaint(img,mask,20,cv2.INPAINT_NS)

cv2.imwrite('inpaint.png',dst23)
