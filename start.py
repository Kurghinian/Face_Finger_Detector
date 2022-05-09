import face_detection
import fingers_A
import color_recognition_A
import fingers_nkar
import cv2

def menu():
    image = cv2.imread("digicode.jpg")
    cv2.putText(image, "1.Color recognition", ( 200, 150), 0, 3, (255, 0, 0), 10)
    cv2.putText(image, "2.Lights control by fingers", ( 200, 300), 0, 3, (0, 0, 0), 10)
    cv2.putText(image, "3.Fingers control in use", ( 200, 450), 0, 3, (0, 0, 255), 10)
    cv2.putText(image, "4.Face recognition", ( 200, 600), 0, 3, (20, 255,0), 10)
    cv2.putText(image, "5.End, Goodbye", ( 200, 750), 0, 3, (205, 15, 250), 10)
    cv2.imshow("image",image)
    
    key = cv2.waitKey(0)
    if key == ord("1"):
        cv2.destroyAllWindows()
        color_recognition_A.cra()
    if key == ord("2"):
        cv2.destroyAllWindows()
        fingers_A.fa()
    if key == ord("3"):
        cv2.destroyAllWindows()
        fingers_nkar.fi()
    if key == ord("4"):
        cv2.destroyAllWindows()
        face_detection.fd()
    if key == ord("5"):
        cv2.destroyAllWindows()
    if key != ord("5"):
        menu()
menu()

