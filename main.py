import pyqrcode

url = input("enter url to generate QR Code: ")
qr_code = pyqrcode.create(url)
qr_code.svg("qrcode.svg", scale=8)