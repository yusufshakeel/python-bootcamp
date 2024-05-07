import qrcode


def go():
    try:
        input_text = input('Enter text: ')
        qr = qrcode.QRCode(box_size=10, border=4)
        qr.add_data(input_text)
        img = qr.make_image(fill_color='black', back_color='white')
        img.save('qrcode.png')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    go()
