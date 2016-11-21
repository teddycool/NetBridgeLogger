__author__ = 'teddycool'

import time
from Actuators import LedIndicator
#Global GPIO used by all...
import RPi.GPIO as GPIO
from LoggerConfig import config
from Wan import InternetDetection
from Lan import LanConnections



class MainLoop(object):
    def __init__(self):
        #TODO: fix logging to file readable from web
        GPIO.setmode(GPIO.BCM)
        self._onLed =  LedIndicator.LedIndicator(GPIO, config["IO"]["GreenLed"])
        self._inet = InternetDetection.InternetDetection(GPIO, config["IO"]["RedLed"])
        self._lanLed =  LanConnections.DevicesIndicator(GPIO, config["IO"]["YellowLed"])
        self._btLed = LedIndicator.LedIndicator(GPIO, config["IO"]["BlueLed"])
        self._logLed = LedIndicator.LedIndicator(GPIO, config["IO"]["WhiteLed"])

    def initialize(self):
        print "Main init..."
        #self._inputs.initialize()
        self.time=time.time()
        self._onLed.activate()
        self._inet.initialize()
        self._lanLed.initialize()
        self._btLed.activate(False)
        self._logLed.activate(False)

    def update(self):
        start = time.time()
        self._inet.update()
        print "Main update time: " + str(time.time() - start)


    def __del__(self):
        #self._onLed.activate(False)
        GPIO.cleanup()