#send notion info to arduino
from notion import freq_names
import json
import serial

freq_names = json.dumps(freq_names);
print(freq_names)

#todo:
#  pip install serial
#  send freq_names as string to arduino
#  automate code to run every hour