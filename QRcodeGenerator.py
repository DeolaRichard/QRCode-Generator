# importing the neccessary library using pip install qrcode Image.
import qrcode


# Creating a function that collects a text and then converts it to a qrcode.
def generate_qrcode(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4

    )
    qr.add_data(text)
    qr.make(fit=True)
    # save the qr code as an image.
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr_image01")


# get input text from user
url = input("Enter your url: ")
generate_qrcode(url)
