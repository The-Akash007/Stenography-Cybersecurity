# -*- coding: utf-8 -*-
import cv2
import numpy as np
import cv2_imshow

# Upload image manually 
import files
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
c = {i: chr(i) for i in range(255)}

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

# Decryption process
message = ""
n, m, z = 0, 0, 0
pas = input("Enter passcode for Decryption: ")

if password == pas:
    for i in range(len(msg)):
        message += c[img[n, m, z]]
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT AUTHORIZED!")
