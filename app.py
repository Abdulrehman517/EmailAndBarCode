import qrcode
import cv2
obj = qrcode.make('www.youtube.com')
obj.save('barcode.jpg')
de = cv2.QRCodeDetector()
val, _, _ = de.detectAndDecode(cv2.imread('barcode.jpg'))
print("decode text is: ", val)
