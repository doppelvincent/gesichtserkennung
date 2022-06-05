from ast import increment_lineno
import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread("bild.jpg")
print(img[0][0])
# i = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# print(img.shape) # zeile, spalte, 3.Wert sind Farbkanäle (RGB), openCV liest den Farbcode als BGR



g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #bei Graustufen haben wir einen Wert weniger bei shape
print(g.shape)

plt.imshow(g, "gray")
plt.show()
