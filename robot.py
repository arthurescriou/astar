# à lancer sur le robot
import serial
from time import sleep
import os


robotPort = os.popen('ls /dev/ttyACM*').read().strip()
print("Found serial : " + robotPort)

def openSerial():
    return serial.Serial(robotPort)

def sendInstruction(char, ser):
    ser.write(char.encode())


ser = openSerial()

for i in range(10):
    sleep(1/(i+1))
    sendInstruction('z', ser)


ser.close()
