# COVERTOVERT Project Report

## Aim of the Application
The COVERTOVERT project is designed to demonstrate communication between two machines using ICMP (Internet Control Message Protocol) packets. The application is implemented using Python and the Scapy library, running within a Docker Compose setup to simulate separate sender and receiver machines. The sender generates and sends ICMP packets, while the receiver listens for and processes these packets.

## Code Explanation

### `icmp_receiver.py`
**Important Logic**:
- **Packet Sniffing**: The `receive()` method uses `scapy.all.sniff(count=1, filter="icmp", prn=lambda x: filter_list.append(x))` to capture ICMP packets.
  - **`count=1`**: Specifies that only one packet should be captured at a time.
  - **`filter="icmp"`**: Ensures that only ICMP packets are captured, filtering out other types of network traffic.
  - **`prn=lambda x: filter_list.append(x)`**: Defines a callback function that appends the captured packet to `filter_list`. This allows the program to store and process the packet once captured.

### `icmp_sender.py`
**Important Logic**:
- **Packet Creation**: The line `pack = scapy.all.IP(dst="receiver", ttl=1) / scapy.all.ICMP()` constructs an IP packet with an ICMP layer.
  - **`dst="receiver"`**: Sets the destination of the packet. This should be the address of the target machine.
  - **`ttl=1`**: Specifies the Time-To-Live (TTL) value, limiting the packet's hop count to one. This is used to control how far the packet can travel in the network.
    - The hop count refers to the number of intermediate devices (such as routers) that a packet passes through from its source to its destination within a network. Each time a packet moves from one device to the next, it counts as one "hop."


  - **`/ scapy.all.ICMP()`**: Adds an ICMP layer to the packet, indicating that it is an ICMP packet.

- **Packet Sending**: The `send()` function is used to transmit the packet to the destination.

## Group Information
- **Name**: Mert Uludoğan
- **Student ID**: 2380996
- **Group ID**: <Your Group ID>

## GitHub Repository
Link to the forked repository from 'covertovert':
[GitHub Repository Link](<insert your GitHub link here>)

