import pyqrcode
from pyqrcode import QRCode

# string which represent the QR code

s = "https://www.youtube.com/watch?v=QH2-TGUlwu4"

# Generate QR code
url = pyqrcode.create(s)

# create and save the png file naming "myqr.png"
url.svg("myqr.svg", scale=8)
