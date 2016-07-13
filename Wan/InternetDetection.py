__author__ = 'teddycool'
#http://stackoverflow.com/questions/17304225/how-to-detect-if-computer-is-contacted-to-the-internet-with-python
#Handle check of internetconnection and turning on/off a indication led
import os
import Time
import urllib2
try:
    from LoggerConfig import config
except:
    config = {
              "InternetDetection": {"URL": "http://www.google.com",},
              }

class InternetDetection(object):

    def __init__(self):
        print "Init"
        #TODO: fix indicator led


    def initialize(self):
        print "Initialize"


    def update(self):
        #TODO: set timeinterval for checking

        try:
            urllib2.urlopen(config["InternetDetection"]["URL"]).close()
            print "Connected"
        except:
            print "Not Connected"



if __name__ == '__main__':
    print "Testcode for NetDetector"
    nd = InternetDetection()
    nd.initialize()
    while(True):
        nd.update()
        Time.sleep(1)