import time
import cv2
import webbrowser
from urllib.parse import urlparse

cam=cv2.VideoCapture(0)
cam.set(5,1280)
cam.set(6,720)
detector=cv2.QRCodeDetector()
camera=True
while camera==True:
    success,frame=cam.read()
    data,one,_=detector.detectAndDecode(frame)
    if data:
        a=data.strip()
        url_parse=urlparse(a)
        if url_parse.scheme in ['http','https']:
          webbrowser.open(a)
        else:
          print(f"Scan Qr Code: {a}")
          break
    cv2.imshow("QR_Scanner",frame)

    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()