import socket
import sys
import time

class UDP_data:
    s  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDP_IP = ""
    UDP_PORT = 0
    def start(self,ip_address,port,socket_type):
        UDP_data.UDP_IP = ip_address
        UDP_data.UDP_PORT = port
        try :
            UDP_data.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            UDP_data.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            UDP_data.s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) ## depends
        except:
            print('Failed to create socket')
            sys.exit()
        if(socket_type == 'receive'):
            try:
                UDP_data.s.bind((ip_address, port))
            except:
                print('Bind failed.')
                sys.exit()

        print('Server listening')
        return

    def update(self):
            data,ADDR = UDP_data.s.recvfrom(1024)
            count = 0
            if(count == 0):
                #print("started receiving")
                count = count+1
            return data

    def send(self,msg):
        UDP_data.s.sendto(msg,(UDP_data.UDP_IP,UDP_data.UDP_PORT))

    def stop(self):
            UDP_data.s.close()
