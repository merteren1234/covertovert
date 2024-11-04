import scapy
import scapy.all

class icmp_receiver:
    def __init__(self):
        self.receive()
        
    def receive(self):
        filter_list=[]
        flag=True
        while flag==True:
            scapy.all.sniff(count=1,filter="icmp",prn=lambda x:filter_list.append(x))
            if(filter_list[0].ttl==1):
                flag=False
            else:
                filter_list.pop()
        filter_list[0].show()

# icmp_receiver() // uncomment this line to run the code