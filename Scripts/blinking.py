from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

while True:
 sense.clear((255, 255, 255))
 sleep(0.5)
 sense.clear((0, 0, 0))
 sleep(0.5)
