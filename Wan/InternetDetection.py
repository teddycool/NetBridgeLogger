__author__ = 'teddycool'
#http://stackoverflow.com/questions/17304225/how-to-detect-if-computer-is-contacted-to-the-internet-with-python
#Handle check of internetconnection and turning on/off a indication led
import os
import time
import urllib2
from Actuators import LedIndicator
try:
    from LoggerConfig import config
except:
    config = {
              "InternetDetection": {"URL": "http://www.google.com","TimeSlot":1},
              }

class InternetDetection(object):

    def __init__(self, GPIO, io):
        print "Init"
        self._lastCheck = 0 #Force check at first update
        #TODO: fix indicator led
        self._iLed = LedIndicator.LedIndicator(GPIO, io)


    def initialize(self):
        print "Initialize"
        self._iLed.activate(False)


    def update(self):
        #TODO: set timeinterval for checking
        if time.time() - self._lastCheck > config["InternetDetection"]["TimeSlot"]:
            try:
                urllib2.urlopen(config["InternetDetection"]["URL"]).close()
                print "Connected"
                self._iLed.activate(True)
            except:
                print "Not Connected"
                self._iLed.activate(False)
            self._lastCheck = time.time()


    def __del__(self):
        self._iLed.activate(False)


if __name__ == '__main__':
    print "Testcode for NetDetector"
    nd = InternetDetection()
    nd.initialize()
    while(True):
        nd.update()
        time.sleep(1)