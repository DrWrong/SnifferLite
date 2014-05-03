#! /usr/bin/env python
# coding:utf-8

from scapy.sendrecv import sniff
from multiprocessing import Process


class SnifferProcess(Process):

    def __init__(self, queue, sniff_filter=None, iface=None, *args, **kwargs):
        super(SnifferThread, self).__init__(*args, **kwargs)
        self.filter = sniff_filter
        self.iface = iface
        self.daemon = True
        self.queue = queue

    def run(self):
        while True:
            pkts = sniff(iface=self.iface, filter=self.filter, count=5)
            self.queue.put(pkts)
