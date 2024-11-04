import scapy
import scapy.all


# when the reciever reaches the max_packet_count with target ttl, it will stop receiving packets
class icmp_receiver:
    max_packet_count = 3
    target_ttl = 1
    def __init__(self):
        self.receive()

    def receive(self):
        filter_list = []
        ttl_one_count = 0  # Track the count of TTL=1 packets

        while ttl_one_count < self.max_packet_count:
            scapy.all.sniff(count=1, filter="icmp", prn=lambda x: filter_list.append(x))
            packet = filter_list.pop()  # Retrieve the latest packet

            # Check if the packet's TTL is 1
            if packet.ttl == self.target_ttl:
                ttl_one_count += 1
                print("Received proper packet")  # Print message for each TTL=1 packet

icmp_receiver()
