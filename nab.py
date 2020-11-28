from scapy.all import *

def findRemy(pkt):
    print(pkt['Raw'].load)
    return pkt