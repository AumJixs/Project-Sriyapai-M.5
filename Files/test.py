import time
from pymata4 import pymata4
import sys

trigger = 9
echo = 10

pin = 12

board = pymata4.Pymata4()

def the_callback(data):
    print("distance :",data[2])

def servo(my_board, pin ):
    """
    Set a pin to servo mode and then adjust
    its position.

    :param my_board: pymata4
    :param pin: pin to be controlled
    """

    # set the pin mode
    my_board.set_pin_mode_servo(pin)

    # set the servo to 0 degrees
    my_board.servo_write(pin, 0)
    time.sleep(1)
    # set the servo to 90 degrees
    my_board.servo_write(pin, 180)
    time.sleep(1)
    # set the servo to 180 degrees

board.set_pin_mode_sonar(trigger , echo , the_callback)

while True:
    try:
        #servo(board, 12)
        time.sleep(5)
        board.sonar_read(trigger)
    except Exception:
        board.shutdown()
        sys.exit(0)