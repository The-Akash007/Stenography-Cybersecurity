# Stenography-Cybersecurity
Steganography is a technique used in cybersecurity to hide information within other files or messages. It can be used to hide text, images, videos, or audio. 
# Secure Data Hiding in Images By Image Steganography using Python and OpenCV

This project demonstrates a simple implementation of image steganography using Python and OpenCV. It allows users to hide (encrypt) a secret message inside an image and later retrieve (decrypt) the message using a Tkinter-based graphical user interface (GUI).

## Features

### Data Hiding (Encryption):
- Embed a secret text message into a cover image.
- The program writes each character's ASCII value into the image pixels using a diagonal embedding method.
- Saves the modified image as a lossless PNG file to preserve data integrity.

### Decryption:
- Retrieve the hidden message from the modified image.
- Requires the correct passcode and message length for successful extraction.


## Requirements
Ensure you have the following dependencies installed before running the scripts:

```bash
pip install opencv-python tkinter
```

## Usage

### 1. Encrypting a Message
To hide a secret message in an image:

```bash
python encrypt.py
```

**Steps:**
1. The script will ask for the image file (e.g., `mypic.jpg`).
2. Enter the secret message you want to hide.
3. Provide a password for security.
4. The encrypted image is saved as `encryptedImage.png`.
5. The password is stored in `key.txt`.

### 2. Decrypting a Message
To retrieve the hidden message from the encrypted image:

```bash
python decrypt.py
```

**Steps:**
1. The script reads `encryptedImage.png`.
2. You must enter the correct password.
3. If the password matches, the hidden message is displayed.
4. If the password is incorrect, access is denied.

## File Descriptions
- **`encrypt.py`** - Script to embed a secret message into an image.
- **`decrypt.py`** - Script to extract the secret message from the image.
- **`encryptedImage.png`** - Image containing the hidden message.
- **`key.txt`** - Stores the password required for decryption.
- **`mypic.jpg`** - Original image used for encryption.

## Example
### Encrypting:
```bash
Enter secret message: Hello, world!
Enter a passcode: mysecretpass
Encryption done. Saved as 'encryptedImage.png'.
```

### Decrypting:
```bash
Enter password: mysecretpass
Secret message: Hello, world!
```

## License
This project is open-source and available under the MIT License.

## Author
Your Name

Akash Rajendra Bambal
