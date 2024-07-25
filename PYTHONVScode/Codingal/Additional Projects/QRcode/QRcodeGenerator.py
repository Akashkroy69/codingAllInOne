import qrcode
from PIL import Image

data = "https://akashkumarroyblog.wordpress.com/"

qr = qrcode.QRCode(version = 1, box_size=10,border=5)
qr.add_data(data)
qr.make(fit=True)

image = qr.make_image(fill="white",back_color="white")
image.save("qr_code.png")
image.show()