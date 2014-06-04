#! /usr/bin/env python
# coding:utf-8

from scapy.all import sniff, wrpcap, Scapy_Exception
from threading import Thread, Lock
import logging
from mongokit import Document, Connection
import datetime
# import string

connection = Connection()


@connection.register
class PacketDocument(Document):
    __database__ = 'snifferlite'
    __collection__ = 'packet'
    structure = {
        'srcip': basestring,
        'destip': basestring,
        'summary': basestring,
        'time': datetime.datetime,
        'detail': basestring,
    }
    default_values = {'time': datetime.datetime.now()}

logging.basicConfig(
    filename="snifferlite.log",
    format="%(levelname)-10s %(asctime)s %(message)s",
    level=logging.DEBUG
)
logger = logging.getLogger('snifferlite.sniffprocess')


class SnifferProcess(Thread):

    def __init__(self, queue, sniff_filter='', iface=None, outfile=None, *args, **kwargs):
        super(SnifferProcess, self).__init__(*args, **kwargs)
        self._filter = sniff_filter
        if not self._filter:
            self._filter = 'not icmp and not arp'
        self.iface = iface
        self.daemon = True
        self.queue = queue
        self._terminate = False
        self._suspend_lock = Lock()
        self.outfile = outfile

    def run(self):
        while True:
            if self._terminate:
                break
            self._suspend_lock.acquire()
            self._suspend_lock.release()
            try:
                sniff(iface=self.iface, count=1,
                     filter=self._filter, prn=self.processpacket)
            except Scapy_Exception:
                self._filter = 'not icmp and not arp'
    def terminate(self):
        self._terminate = True

    def suspend(self):
        self._suspend_lock.acquire()

    def resume(self):
        self._suspend_lock.release()

    def changefilter(self, filterstring):
        self._suspend_lock.acquire()
        self._filter = filterstring
        self._suspend_lock.release()

    def processpacket(self, packet):
        # packet.show()
        #
        # packet.summary()
        # print type(packet)
        # packet.show()

        self.queue.put(packet)
        packtdocument = connection.PacketDocument()
        #print(packtdocument)
        packtdocument['srcip'] = packet.sprintf('%IP.src%')
        packtdocument['destip'] = packet.sprintf('%IP.dst%')
        packtdocument['summary'] = packet.summary()
        packtdocument['detail'] = packet.command()
        packtdocument.save()
        #print(packtdocument)
        if self.outfile:
            wrpcap(self.outfile, packet, append=True)
