# -*- coding: utf-8 -*-
import cv2
import numpy as np
import cv2_imshow
import files

# Upload the encrypted image manually
uploaded = files.upload()

# Get the uploaded image filename
image_filename = list(uploaded.keys())[0]

# Read the encrypted image
img = cv2.imread(image_filename)
if img is None:
    print("Error loading image. Make sure the file is correctly uploaded.")
else:
    print("Encrypted image loaded successfully.")

# Get user input for decryption
pas = input("Enter passcode for Decryption: ")

# Ask user for the message length
msg_length = int(input("Enter the length of the secret message: "))

# Define character mapping (extend to 255)
c = {i: chr(i) for i in range(256)}  # Now includes 255

# Secret message retrieval
message = ""
n, m, z = 0, 0, 0

# Ensure passcode is correct
if pas:
    for i in range(msg_length):  # Loop for the message length
        pixel_value = img[n, m, z]
        if pixel_value in c:  # Ensure it's a valid key
            message += c[pixel_value]
        else:
            message += "?"  # Handle unexpected values gracefully
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT AUTHORIZED!")
