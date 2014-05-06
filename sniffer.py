#! /usr/bin/env python
# coding:utf-8

from scapy.sendrecv import sniff
from multiprocessing import Process


class SnifferProcess(Process):

    def __init__(self, queue, sniff_filter='', iface=None, *args, **kwargs):
        super(SnifferProcess, self).__init__(*args, **kwargs)
        self._filter = sniff_filter
        if not self._filter:
            self._filter = 'not icmp and not arp'
        self.iface = iface
        self.daemon = True
        self.queue = queue

    def run(self):
        while True:
            pkts = sniff(iface=self.iface, filter=self._filter, count=1)
            self.queue.put(pkts)
