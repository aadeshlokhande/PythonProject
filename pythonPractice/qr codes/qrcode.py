# Import QRCode from pyqrcode
import pyqrcode
# import png
# from pyqrcode import QRCode
s = "hello"
url = pyqrcode.create(s)
url.png(f'myqr.png', scale = 50)