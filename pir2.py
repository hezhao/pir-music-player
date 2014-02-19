import time
from subprocess import Popen
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)
GPIO.setup(12, GPIO.IN)

pir_state = False
proc = None
song = 'snow-6sec.mp3'

def isPlaying():
    if proc is None:
        return False
    retcode = proc.poll()
    if retcode is None:
        return True
    return False

while True:
    val1 = GPIO.input(8)
    val2 = GPIO.input(12)
    if val1 == True or val2 == True:
	# print 'led on!'
        if pir_state == False:
            print 'motion detected!'
            # if music is not playing, play music here
            if not isPlaying():
                pir_state = True
                proc = Popen(['/usr/bin/mpg123', song])
    else:
        # print 'led off!'
        if pir_state == True:
            print 'motion ended!'
            pir_state = False
    time.sleep(0.01)

