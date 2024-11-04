import scapy
import scapy.all
import random
import time

# merhaba
# sends 10 packets with TTL=1 and TTL=2 values
class icmp_sender:
    def __init__(self):
        self.send_packets()

    def send_packets(self):
        # Generate a list of 3 TTL=1 and 7 TTL=2 values, then shuffle the list
        ttl_values = [1] * 3 + [2] * 7
        random.shuffle(ttl_values)

        # Send each packet according to the randomized TTL values
        for ttl in ttl_values:
            pack = scapy.all.IP(dst="receiver", ttl=ttl) / scapy.all.ICMP()
            scapy.all.send(pack)
            print(f"Sent packet with TTL={ttl}")
            time.sleep(1)  # Wait for 1 second between sends

icmp_sender()
