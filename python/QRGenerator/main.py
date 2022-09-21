import qrcode
from PIL import Image

class QRCode():
    def generateQRCode(text):
        qr = qrcode.QRCode(
            # 21x21 matrix
            version=1, 
            # 7% or less errors corrected
            error_correction = qrcode.ERROR_CORRECT_L,
            # 10 pixels wide
            box_size=10,
            # border thickness
            border=4,
        )
        # make the QR Image that points to our link
        qr.add_data(text)
        qr.make(fit=True)
        image = qr.make_image(fillcolor="black", back_color="white")
        image.save("QRImage.png")

    def openQRImage():
        qrImage = Image.open(r"C:\Users\Abraham\Documents\GitHub\Samples\QRImage.png")
        qrImage.show()

def main() -> None:
    # generate QR Code for this link
    QRCode.generateQRCode("https://musicforprogramming.net/latest/")
    # Show the generated image
    QRCode.openQRImage();

if __name__ == "__main__":
    main()