from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog

# get key and token (encrypted text)
root = tk.Tk()
root.withdraw()

key_path = filedialog.askopenfilename(title="Select key file")
token_path = filedialog.askopenfilename(title="Select token file")

# if key and token are located within the same folder as decrypt.py
# (encrypt.py creates them in the same folder by default),
# comment the above two lines out and uncomment the two lines below
# it will skip the file dialog and just grab the key and token files directly

# key_path = "./key.key"
# token_path = "./encrypted.txt"

f = open('decryptedtoken.txt', 'a') # file for original text

key_file = open(f'{key_path}', 'rb')
token_file = open(f'{token_path}', 'rb')

key = key_file.read()
token = token_file.read()

# changed to bin file, see if it works
# key_str = key[2:-1] # remove the remove the b'' from the key string (ex. b'key')
# print(key_str)
# print(type(key_str))
# key_bytes = key_str.encode('utf-8')

# print(key_bytes)
# print(type(key_bytes))

# fkey = Fernet(key_bytes)
fkey = Fernet(key)
print(fkey)
print(token)
decrypted_token = fkey.decrypt(token).decode('utf-8')

print(decrypted_token)