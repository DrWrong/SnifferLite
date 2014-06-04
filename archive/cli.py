#! /usr/bin/env python
# coding:utf-8
from optparse import OptionParser
from macflood import start_attack
from arp import ARP_ATTACK
from set_promisc_mode import PromiscModel
from sniffer import SnifferProcess
from scapy.all import conf
##configer input option and parse it
p = OptionParser()
p.add_option("-i", "--interface", type="string", default='eth0', dest="interface")
p.add_option("-f", '--filter', type="string", dest="filter")
p.add_option("-m", "--mode", type="choice", choices=['negtive', 'arp_mode', 'mac_flood_mode'], default='negtive', dest="mode")
p.add_option("--gui", action="store_true", dest="guimode")
opt, args = p.parse_args()


def sniffer_prepare(opt):
    pass
#    if opt.mode == 'arp_mode':
#        arp1 = ARP_ATTACK(ifname=opt.interface)
#        arp2 = ARP_ATTACK(attact_type=0, ifname=opt.interface)
#        arp1.start()
#        arp2.start()
#    elif opt.mode == 'mac_flood_mode':
#        
#        macfloodlist = start_attack(ifname=opt.interface)
    #conf.set_promisc_mode = True

