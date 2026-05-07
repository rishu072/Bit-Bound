import qrcode
from qrcode.constants import ERROR_CORRECT_L

print("------QR code generator------")
while True:
    data=input(' Enter the test or url for QR code: ')

    file_name=input('Enter the file name to save the QR code (without extension): ')
    file_color=input('Enter the color for the QR code (e.g., black, red, blue): ')
    back_color=input('Enter the back color for the QR code (e.g., white, yellow, lightgray): ')

    qr=qrcode.QRCode(version=1,error_correction=ERROR_CORRECT_L,box_size=10,border=4)
    qr.add_data(data)
    qr.make(fit=True)

    img=qr.make_image(fill_color=file_color,back_color=back_color)
    img.save(f'{file_name}.png') 

    print(f'QR code generated and saved successfully as {file_name}.png')
    
    ch = input('Do you want to generate another QR code? (y/n): ')
    if ch.lower() != 'y':
        print("thank you for using the QR code generator. Goodbye!")
        break