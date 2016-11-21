__author__ = 'teddycool'


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

if __name__ == "__main__":
    cd=Main()
    cd.run()
