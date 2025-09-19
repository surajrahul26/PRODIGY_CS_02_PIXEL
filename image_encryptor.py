from PIL import Image
import numpy as np

#Encryption function
def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    img_array = np.array(image)

    # XOR each pixel with the key
    encrypted_array = img_array ^ key
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_image.save(output_path)
    print("Image encrypted and saved to", output_path)

#Decryption function (same as encryption for XOR)
def decrypt_image(input_path, output_path, key):
    encrypt_image(input_path, output_path, key)  # XOR again to decrypt

#Example usage
key = 123  # We can choose any integer between 0–255
encrypt_image("sample.jpg", "encrypted_image.png", key)
decrypt_image("encrypted_image.png", "decrypted_image.png", key)