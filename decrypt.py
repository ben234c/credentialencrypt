from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog

# get key and token (encrypted text)
root = tk.Tk()
root.withdraw()

key_path = filedialog.askopenfilename(title="Select key file")
token_path = filedialog.askopenfilename(title="Select token file")

f = open('decryptedtoken.txt', 'a')

key = open(f'{key_path}', 'rb')
token = open(f'{token_path}', 'r')

key2 = key.read()
token2 = token.read()

print(key2)
print(type(key2))

# fkey = Fernet()

# plaintext = fkey.decrypt(token)
