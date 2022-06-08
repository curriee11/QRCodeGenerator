
import qrcode
qr=qrcode.QRCode(
    box_size=10,
    version=15,
    border=5
)

data="https://www.linkedin.com/in/khushi-agarwal-b756b61b9/"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save('txt.png')
# save('txt.png')
