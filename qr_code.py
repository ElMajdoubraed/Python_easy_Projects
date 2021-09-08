#pip install PyQRCode
import os
import pyqrcode
from PIL import Image

class Qr_ (object):
         def init_ (self, text):
                  self.qr_image = self.qr_generator(text)

         @staticmethod
         def qr_generator(text):
                  qr_code = pyqrcode.create(text)
                  file_name = "QR Code result"
                  save_path = os.path.join(os.path.expanduser('~'),'Desktop')
                  name = f"{save_path}{file_name}'.png"
                  qr_code.png(name, scale=10)
                  image = Image.open(name)
                  image = image.resize((400,400),Image.ANTIALIAS)
                  image.show()

if __name__ == "__main__" :
         Qr_(input("[QR] Enter text or link: "))
