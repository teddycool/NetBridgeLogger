__author__ = 'teddycool'
#Config vaues for DartScore. This is the only place for these.
#The button is 'on' when holded pressed and IO defined in init is connected to ground
#TODO: Fix values according to IOTest!!!

config = {     "IO": { "GreenLed": 26, "RedLed": 19, "YellowLed": 13, "BlueLed": 6, "WhiteLed": 5, "RedButton": 11},
                "Main": {"MaxFrameRate": 10},
                "InternetDetection": {"URL": "http://www.google.com","TimeSlot":60},
                "Button": {"Pressed": 0.1, "LongPressed": 1.5},               }


