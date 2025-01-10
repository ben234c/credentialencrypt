import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from cryptography.fernet import Fernet
import base64


def textencrypt(user, pw):
    f2 = open('encrypted.txt', 'wb')
    f3 = open('key.key', 'wb')
    cred = f"{user} {pw}" # combine both user and pw
    key = Fernet.generate_key() # make key
    f3.write(key)
    # decoded_key = key.decode('utf-8')
    # print(decoded_key)

    fkey = Fernet(key) # "load" key into Fernet
    token = fkey.encrypt(cred.encode('utf-8'))
    f2.write(token)
    # print(f'{token}')
    
    f2.close()
    f3.close()
    return key, token

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Account Credentials'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 200
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textboxes
        self.textbox = QLineEdit(self, placeholderText="Username")
        self.textbox.move(20, 20)
        self.textbox.resize(140, 25)

        self.textbox2 = QLineEdit(self, placeholderText="Password")
        self.textbox2.move(20, 60)
        self.textbox2.resize(140, 25)

        # Create buttons
        self.button = QPushButton('Submit', self)
        self.button.move(20, 120)

        # Link button to a function on click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        username = self.textbox.text()
        password = self.textbox2.text()
        confirmation = QMessageBox.question(self,'Confirm Credentials', 'You typed: ' + username + ' ' + password, QMessageBox.Yes, QMessageBox.No)
        
        if confirmation == 16384: # Values for the QMessageBox::Yes and No are 16384 and 65536 (Converted from 8-bit hex numbers). https://doc.qt.io/qt-5/qmessagebox.html
           
            # write original plaintext to a file to check later
            f = open('records.txt', 'a')
            f.write(f'\n{username}, {password}') # store plaintext user and pass to double check 
           
            # encrypt given text
            textencrypt(username, password)
            f.close()

            # clear text boxes
            self.textbox.setText('')
            self.textbox2.setText('')
    
    

if __name__=='__main__': # launch app
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_()) ()


