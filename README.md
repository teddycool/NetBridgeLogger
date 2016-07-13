# NetBridgeLogger

Dependencies:
install MJPG-streamer, instructions are found here: https://www.raspberrypi.org/forums/viewtopic.php?t=48597
http://raspberrypihq.com/how-to-turn-a-raspberry-pi-into-a-wifi-router/
http://www.noveldevices.co.uk/rp-dhcp-server
 
NetBridgeLogger is a raspberry pi with a WiFi, Ethernet, BT, a realtime clock and some sensors, leds, buttons and a switch. 
The netbridge-part will connetc wiFi and Ethernet. (IE use an andriod shared internetconnection in a local network)
The logger-part will take information from different sources on the local networks and merge this with an optional 
video output stream with information overlays.

The purpose is to act as a logger in a surveillance system or in other projects where a logger is needed.
Leds are used for displaying operation mode and button and switches for user interaction...





 http://raspberrypihq.com/how-to-turn-a-raspberry-pi-into-a-wifi-router/
 http://stackoverflow.com/questions/17304225/how-to-detect-if-computer-is-contacted-to-the-internet-with-python
 http://www.noveldevices.co.uk/rp-dhcp-server

To view stream:
sudo python Main.py

http://logger-ip:8080/?action=stream 


