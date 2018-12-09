import udp_class
import time
udp = udp_class.UDP_data()
udp.start("127.0.0.1",5005,'receive')
time1 = time.time()
while(time.time()-time1<20):
    data = udp.update()
    print(data)
udp.stop()
print("over")
