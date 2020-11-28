from scapy.all import *

def findRemy(pkt):
    if('remy' in pkt['Raw'].load):
        print(pkt['Raw'].load)
    return pkt