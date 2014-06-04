#! /usr/bin/env python
# coding:utf-8
#from __future__ import print_function
from optparse import OptionParser
from macflood import start_attack
from arp import ARP_ATTACK
# from set_promisc_mode import PromiscModel
from sniffer import SnifferProcess
from scapy.all import conf, hexdump
import Queue
import gui
import re
import sys

stdout = sys.stdout


# configer input option and parse it
Op = OptionParser()
Op.add_option("-i", "--interface", type="string",
              default='eth0', dest="interface")
Op.add_option("-f", '--filter', type="string", dest="filter")
Op.add_option("-o", '--out', type="string", dest="outfile")
Op.add_option("-m", "--mode", type="choice", choices=[
              'negtive', 'arp_mode', 'mac_flood_mode'], default='negtive', dest="mode")
Op.add_option("--gui", action="store_true", dest="guimode")
Opt, args = Op.parse_args()


def sniffer_prepare(opt):
    processlist = []
    if opt.mode == 'arp_mode':
        print('strting arp attack')
        arp1 = ARP_ATTACK(ifname=opt.interface)
        arp2 = ARP_ATTACK(attact_type=0, ifname=opt.interface)
        arp1.start()
        arp2.start()
        processlist.append(arp1)
        processlist.append(arp2)
    elif opt.mode == 'mac_flood_mode':
        print('macflood starting')
        macfloodlist = start_attack(ifname=opt.interface)
        processlist += macfloodlist
    conf.set_promisc_mode = True
    return processlist


def sniffer_mainprocess():
    queue = Queue.Queue()
    processlist = sniffer_prepare(Opt)

    sp = SnifferProcess(queue, Opt.filter, Opt.interface, Opt.outfile)
    sp.start()
    sys.stdout = stdout
    print('stratring sniffer')
    packet_list = []
    while True:

        option = raw_input(
            'plese choose displaymethod press "?" or "h" for help:')
        # print(option)
        m = re.match(r'(filter|f)\s(?P<filterstring>[\w\s]+)', option)
        if m:
            filterstring = m.groupdict()['filterstring']
            sp.changefilter(filterstring)
            continue
        if option == 'show' or option == 's':
            while True:
                try:
                    packet = queue.get()
                    num = len(packet_list)
                    print "%d:   %s" % (num, packet.summary())
                    packet_list.append(packet)
                except KeyboardInterrupt:
                    break
            continue

        m = re.match(r'(display|d)\s(?P<id>\d+)', option)
        if m:
            id = m.groupdict()['id']
            try:
                packet = packet_list[int(id)]
            except IndexError:
                print('choose a valiuable index')
            else:
                packet.show()
                hexdump(packet)
            continue
        if option == 'q':
            for process in processlist:
                process.terminate()
            sp.terminate()
            break
            # continue


        if option in ['?', 'h', 'help']:
            print('''
                s(show)   show the summary of captcure packet
                d(display) num    show the specific of the captcure packet
                f(filter)  change the filter options''')

if __name__ == '__main__':
    if Opt.guimode:
        gui.start_gui()
    else:
        sniffer_mainprocess()
