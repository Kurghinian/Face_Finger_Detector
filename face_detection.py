def fd():
    import cv2
    import pyfirmata
    board = pyfirmata.ArduinoMega('/dev/ttyACM0')
    face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    while True:
        check, frame = cap.read()
        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)
        for x,y,w,h in faces:
            frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
        cv2.imshow('face', frame)
        print(len(faces))
        if len(faces) == 1:
            board.digital[13].write(1)
        elif len(faces) == 2:
            board.digital[13].write(1)
            board.digital[12].write(1)
        elif len(faces) > 2:
            board.digital[13].write(1)
            board.digital[12].write(1)
            board.digital[11].write(1)
        else:
            board.digital[13].write(0)
            board.digital[12].write(0)
            board.digital[11].write(0)
                
         
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


