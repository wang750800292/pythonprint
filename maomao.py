import qrcode 
qr = qrcode.QRCode(     
    version=2,     
    error_correction=qrcode.constants.ERROR_CORRECT_L,     
    box_size=10,     
    border=4, 
) 
qr.add_data('Elegant maomao, I love you!') 
qr.make(fit=True)  
img = qr.make_image()
img.save('maomao.jpg')