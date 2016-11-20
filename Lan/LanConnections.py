#Handle check of connected devices. Number of devices and there IP?
#Blink a led matching number of connected devices
#http://askubuntu.com/questions/219609/how-do-i-show-active-dhcp-leases
from Actuators import LedIndicator
from LoggerConfig import config
import time

class DevicesIndicator(object):
    def __init__(self, GPIO, io):
        self._noDevices = 0
        self._states = ["START","DEVCOUNT", "IDLE"]
        self._starttime = 3     #Time to light led at start
        self._blinktime = 0.5   #Blinktime for each connected device
        self._idletime = 2      #Idletime between sets of device blinkouts...
        self._devLed = LedIndicator.LedIndicator(GPIO, io)
        self._currentState = "START"

    def initialize(self):
        self._devLed.activate(True)
        self._lastactivated = time.time()


    def update(self):
        #if self._currentState == "START":

        return


    def getConnectedDevices(self):
        devices = {}

        return devices

