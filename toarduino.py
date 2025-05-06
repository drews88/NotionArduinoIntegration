#send notion info to arduino
from notion import freq_names
import json
import serial
import time

#print(freq_names)

seri = serial.Serial("/dev/tty.usbmodem1101", 9600)
time.sleep(2)

seri.write((json.dumps(freq_names) + '\n').encode('utf-8'))
seri.close()
