#! /usr/bin/env python
# coding:utf-8

from scapy.sendrecv import sniff
from multiprocessing import Process
import logging
logging.basicConfig(
    filename = "snifferlite.log",
    format = "%(levelname)-10s %(asctime)s %(message)s",
    level = logging.DEBUG
    )
logger = logging.getLogger('snifferlite.sniffprocess')


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
        logger.debug('filter: ' + self._filter)
        logger.debug('iface: '+ self.iface)
        sniff(iface=self.iface, filter=self._filter, prn=self.processpacket)
        
    def processpacket(self, packet):
        self.queue.put(packet)
