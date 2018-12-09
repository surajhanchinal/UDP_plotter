#import socket
import udp_class
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "Hello, World!"
udp = udp_class.UDP_data()
udp.start(UDP_IP,UDP_PORT,'send')
print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

while True:
    name = raw_input("give me data")
    udp.send(name)

udp.stop()