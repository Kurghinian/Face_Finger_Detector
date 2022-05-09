def fi():
    import pyautogui as pag
    import cv2 as cv
    import mediapipe as mp
    from time import sleep
    import sys
    import vlc

    cap = cv.VideoCapture(0)
    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils
    pag.FALLSAFE = False
    erg = vlc.MediaPlayer('/home/pi/Desktop/erg/Queen.mp3')


    if not cap.isOpened():
        print("Cannot open camera")
        sys.exit()

    pag.hotkey('ctrl', 'alt', 't')
    sleep(1)
    pag.typewrite('xdg-open Desktop/rpd-wallpaper/balloon.jpg')
    pag.press('enter')
    sleep(0.2)
    pag.hotkey('shift', 'ctrl', 'q')

    p = [0 for i in range(21)]  # создаем массив из 21 ячейки для хранения высоты каждой точки
    finger = [0 for i in range(4)]  # создаем массив из 4 ячеек для хранения положения каждого пальца

    # функция, возвращающая расстояние по модулю (без знака)
    def distance(point1, point2):
        return abs(point1 - point2)

    while True:
        good, img = cap.read()
        
        if not good:
            print("Can't receive frame (stream end?). Exiting ...")
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

               #
                dist8 = distance(p[4], p[8])
                dist12 = distance(p[4], p[12])
                dist16 = distance(p[4], p[16])
                dist20 = distance(p[4], p[20])
                #
                if 40 > dist8 < min(dist12,dist16,dist20):
                    finger[0] = 1
                    #print("0")
                    pag.press('left')
                    
                else:
                    finger[0] = 0
                if dist12 < min(dist8,dist16,dist20):
                    finger[1] = 1
                    #print(1)
                    pag.press('+')
                else:
                    finger[1] = 0
                if dist16 < min(dist12,dist8,dist20):
                    finger[2] = 1
                    #print("2")
                    pag.press('-')
                else:
                    finger[2] = 0
                if p[4]-p[8]<0:
                    erg.play()
                else:
                    erg.stop()
                #print (p[4])
    

        
        cv.imshow('frame', img)
        
        if cv.waitKey(1) == ord('q'):
            break
    erg.stop()
    cap.release()
    cv.destroyAllWindows()
