import scapy.all as scapy


def netscan(ip):
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broad_req = broadcast/arp_req
    answ = scapy.srp(arp_broad_req, timeout =5, verbose = False)[0]
    print ("IP\t\t\tMACaddr")
    for i in answ:
        print(i[1].psrc + "\t\t" + i[1].hwsrc)
    

netscan("192.168.1.44")
