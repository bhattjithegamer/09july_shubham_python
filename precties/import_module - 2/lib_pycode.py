import qrcode

url = "https://www.google.com/"

qr = qrcode.make(url)
qr.save("qrcode.png")
