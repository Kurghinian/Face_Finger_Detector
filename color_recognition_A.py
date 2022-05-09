def cra():
    import cv2
    import pyfirmata
    board = pyfirmata.ArduinoMega('/dev/ttyACM0')
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    while True:
        _, frame = cap.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        height, width, _ = frame.shape

        cx = int(width / 2)
        cy = int(height / 2)

        # Pick pixel value
        pixel_center = hsv_frame[cy, cx]
        hue_value = pixel_center[0]
        #print(hue_value)   

        color = "Undefined"
        if hue_value < 8:
            color = "RED"
        elif hue_value < 22:
            color = "ORANGE"
        elif hue_value < 45:
            color = "YELLOW"
        elif hue_value < 95:
            color = "GREEN"
        elif hue_value < 131:
            color = "BLUE"
        elif hue_value < 170:
            color = "VIOLET"
        elif hue_value < 200:
            color = "RED"

        pixel_center_bgr = frame[cy, cx]
        b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

        cv2.rectangle(frame, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)
        cv2.putText(frame, color, (cx - 200, 100), 0, 3, (b, g, r), 5)
        cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)
        
        if color == "RED":
            board.digital[13].write(1)
            board.digital[12].write(0)
            board.digital[11].write(0)
        elif color == "GREEN":
            board.digital[12].write(1)
            board.digital[13].write(0)
            board.digital[11].write(0)
        elif color == "BLUE":
            board.digital[11].write(1)
            board.digital[12].write(0)
            board.digital[13].write(0)
        else:
            board.digital[11].write(0)
            board.digital[13].write(0)
            board.digital[12].write(0)
        
        
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
