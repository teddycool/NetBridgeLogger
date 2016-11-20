__author__ = 'teddycool'

# Put up the camera, run calibrate
# Start to play...


import MainLoop
import time


class Main(object):

    def __init__(self):
        print "Init Main object for NetBridgeLogger..."
        self._mainLoop=MainLoop.MainLoop()


    def run(self):
        self._mainLoop.initialize()
        stopped = False
        while not stopped:
            framestarttime = time.time()
            self._mainLoop.update()
            time.sleep(0.1)


# Put in  /etc/rc.local for autostart at boot:
# cd /home/pi/NetBridgLogger
# sudo python Main.py &

#Testcode to run module. Standard Python way of testing modules.
#OBS !! comment out   line 47: "C:\Python27\Lib\site-packages\pygame\_camera_vidcapture.py":
#       #self.dev.setresolution(width, height) on row 49 in:
#
if __name__ == "__main__":
    cd=Main()
    cd.run()
