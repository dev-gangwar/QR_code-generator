import qrcode
#approach 1
information=input('enter content to make qrcode:   => ')
#qr=qrcode.make(information)
#qr.save('qr1.png')

#approach 2
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4)
qr.add_data(information)
qr.make(fit=True)
img=qr.make_image(fill_color='black',black_color='white')
img.save('qr2.png')