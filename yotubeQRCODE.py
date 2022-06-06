# import imghdr
from PIL import Image
import qrcode
qr=qrcode.QRCode(
    box_size=10,
    version=15,
    border=5
)

data="https://www.yourquote.in/poeish-c2jey/quotes"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save('txt.png')
# save('txt.png')