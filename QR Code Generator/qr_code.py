import qrcode

# img = qrcode.make("https://www.youtube.com/@tejasb15")
# img.save("Youtube QR Code.png")

qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=18,border=2)

qr.add_data('www.linkedin.com/in/tejasb15')
qr.make(fit=True)

img = qr.make_image(fill_color="#0077B5",back_color="white")
img.save("QR Code Generator/linkedin Qr Code.jpg")
