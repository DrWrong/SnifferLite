#! /usr/bin/env python
# coding:utf-8

from scapy.sendrecv import sniff
from scapy.all import IP
from multiprocessing import Process, JoinableQueue
import logging
from utils import show_in_dict
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
        logger.debug('iface: '+ str(self.iface))
        sniff(iface=self.iface, filter=self._filter, prn=self.processpacket)

    def processpacket(self, packet):
        #print(str(type(packet)))
        logger.debug('packet:'+str(packet))
        showdict = show_in_dict(packet)
        responsedict={
            "src": showdict.get('src', '')+"("+packet.src+")",
            "dst": showdict.get('dst', '')+"("+packet.dst+")",
            "proto": showdict.get('proto'),
            "desc": packet.summary()
        }
        self.queue.put(responsedict)


if __name__ == '__main__':
    queue = JoinableQueue()
    sniffer = SnifferProcess(queue, iface='en1')
    sniffer.start()
    while True:
        packet = queue.get()
        print (str(packet))
        packet.summary()
