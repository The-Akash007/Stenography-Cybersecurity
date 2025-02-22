# -*- coding: utf-8 -*-
"""Encryption Stenography.ipynb

import cv2
import numpy as np
import cv2_imshow
import files

# Upload image manually
uploaded = files.upload()

# Get the uploaded image filename
image_filename = list(uploaded.keys())[0]

# Read the image
img = cv2.imread(image_filename)
if img is None:
    print("Error loading image. Make sure the file is correctly uploaded.")
else:
    print("Image loaded successfully.")

# Get user inputs
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

d = {chr(i): i for i in range(255)}
n, m, z = 0, 0, 0

for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = (n + 1) % img.shape[0]
    m = (m + 1) % img.shape[1]
    z = (z + 1) % 3

# Save and display the encrypted image
encrypted_filename = "encryptedImage.jpg"
cv2.imwrite(encrypted_filename, img)
cv2_imshow(img)
print("Encrypted image saved as", encrypted_filename)
