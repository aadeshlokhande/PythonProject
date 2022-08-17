import io 
import qrcode 
qr = qrcode.QRCode()
qr.add_data("Hello world")
f = io.StringIO()
qr.print_ascii(out = f)
f.seek(0)
print(f.read())

# pip install -e git+git://github.com/ojii/pymaging.git#egg=pymaging
# pip install -e git+git://github.com/ojii/pymaging-png.git#egg=pymaging-png