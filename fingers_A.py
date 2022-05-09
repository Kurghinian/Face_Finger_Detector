def fa():
    import mediapipe as mp
    import cv2 as cv
    import sys
    import pyfirmata

    cap = cv.VideoCapture(0)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
    if not cap.isOpened():
        print("Cannot open camera")
        sys.exit()

    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils
    board = pyfirmata.ArduinoMega('/dev/ttyACM0')

    p = [0 for i in range(21)]  

    def distance(point1, point2):
        return abs(point1 - point2)

    while True:
        good, img = cap.read()
        if not good:
            print("Exiting")
            break
        
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
                for id, point in enumerate(handLms.landmark):
                    width, height, color = img.shape
                    width, height = int(point.x * height), int(point.y * width)
                    p[id] = height

               #################################
                dist8 = distance(p[4], p[8])####
                dist12 = distance(p[4], p[12])##
                dist16 = distance(p[4], p[16])##
                ################################

                if 30 > dist8 < min(dist12, dist16):
                    print(13)
                    board.digital[13].write(1)
                else:
                    board.digital[13].write(0)

                if dist12 < min(dist8, dist16):
                    print(12)
                    board.digital[12].write(1)
                else:
                    board.digital[12].write(0)

                if dist16 < min(dist12, dist8):
                    board.digital[11].write(1)
                    print(11)
                else:
                    board.digital[11].write(0)


        cv.imshow('frame', img)
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()
