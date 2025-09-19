# 🖼️ Image Encryption & Decryption Tool

A simple Python project that demonstrates **image encryption and decryption** using pixel manipulation (XOR operation).  
This project is great for beginners exploring Python, NumPy, and Pillow (PIL).

---

## 🔑 Features
- Encrypts images with a custom numeric key (0–255).
- Decrypts back to the original using the same process.
- Beginner-friendly and easy to understand.

---

## ⚙️ How It Works
1. Load the image with Pillow.
2. Convert it into a NumPy array.
3. Apply XOR operation on each pixel with the chosen key.
4. Save the encrypted/decrypted image.

---

## 📂 Files in this repo
- `image_encryptor.py` → Main script for encryption & decryption.
- `sample.jpg` → Example input image.
- `encrypted_image.png` → Output after encryption.
- `decrypted_image.png` → Restored image after decryption.

---

## ▶️ Run the project
