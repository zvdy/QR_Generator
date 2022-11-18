# python QR code generator given an URL

import pyqrcode


# QR code generator
def qr_code_generator(url):
    qr = pyqrcode.create(url)
    # save the QR code as a png file
    qr.png("qr_code.png", scale=8)


# main function
def main():
    url = input("Enter the URL: ")
    qr_code_generator(url)

if __name__ == "__main__":
    main()