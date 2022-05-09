import pyfirmata
board = pyfirmata.ArduinoMega('/dev/ttyACM0')

board.digital[11].write(0)
board.digital[12].write(0)
board.digital[13].write(0)