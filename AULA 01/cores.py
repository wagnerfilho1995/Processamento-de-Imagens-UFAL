# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

#%%
import cv2
import matplotlib.pyplot as plt
import numpy as np

#%%
img = cv2.imread('onepiece.jpeg', cv2.IMREAD_GRAYSCALE)
plt.imshow(img, cmap='gray')

#%%
img = cv2.imread('onepiece.jpeg', cv2.IMREAD_GRAYSCALE)
img = cv2.cvtColor(img, cv2.IMREAD_COLOR)
plt.imshow(img)

#%%
rgb = cv2.split(img)
plt.subplot(221), plt.imgshow(img)
plt.subplot(222), plt.title('R'), plt.imshow(rgb[0], cmap='gray')
plt.subplot(223), plt.title('G'), plt.imshow(rgb[1], cmap='gray')
plt.subplot(224), plt.title('B'), plt.imshow(rgb[2], cmap='gray')
plt.show()

#%%
img = cv2.imread('download.jpeg', cv2.IMREAD_GRAYSCALE)
plt.subplot(221), plt.title('Original'), plt.imshow(img, cmap='gray')
plt.subplot(222), plt.title('Histogram'), plt.hist(img.ravel(), 256, [0,256])
plt.show()