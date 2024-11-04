import scapy
import scapy.all

class icmp_sender:
    def __init__(self):
        self.sentPacket()


    def sentPacket(self):
        pack=scapy.all.IP(dst="receiver",ttl=1)/scapy.all.ICMP()
        scapy.all.send(pack)

# icmp_sender()
# Implement your ICMP sender here