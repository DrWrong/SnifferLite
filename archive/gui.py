#! /usr/bin/env python
# coding:utf-8
import sys
from PyQt4 import QtGui, QtCore
from ui import Ui_MainWindow
from sniffer import SnifferProcess
import multiprocessing
import netifaces
import logging
from cli import sniffer_prepare
import time
import threading

logging.basicConfig(
    filename = "snifferlite.log",
    format = "%(levelname)-10s %(asctime)s %(message)s",
    level = logging.DEBUG
    )
log = logging.getLogger('snifferlite.gui')

class Param_To_Cli(object):
    def __init__(self):
        self.interface = ''
        self.mode = ''
        self.filter = ''


class StartQT4(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.clidict = Param_To_Cli()
        self.ui.interface_choice.addItems(netifaces.interfaces())
        QtCore.QObject.connect(
            self.ui.start, QtCore.SIGNAL("clicked()"), self.start_sniffer)
        QtCore.QObject.connect(
            self.ui.action_stop, QtCore.SIGNAL("triggered()"), self.stop_sniffer)
        #self.ui.packet_list.setHorizontalHeaderLabels(['时间','源地址','目的地址','内容'])
#        QtCore.QObject.connect(
#            self.ui.interface_choice, QtCore.SIGNAL("activated(const QString&)"), self.get_interface)
#
#        QtCore.QObject.connect(
#            self.ui.mode_choice, QtCore.SIGNAL("activated(const QString&)"), self.get_mode)
#        QtCore.QObject.connect(
#            self.ui.lineEdit, QtCore.SIGNAL("editingFinished()"), self.get_filter)
        

    def start_sniffer(self):
        self.clidict.interface = str(self.ui.interface_choice.currentText())
        self.clidict.mode = str(self.ui.mode_choice.currentText())
        self.clidict.filter = str(self.ui.lineEdit.text())
        log.debug(self.clidict.interface + '' + self.clidict.mode + '' + self.clidict.filter)
        sniffer_prepare(self.clidict)
        self.sniff_queue = multiprocessing.JoinableQueue()
        self.sniffer = SnifferProcess(self.sniff_queue, iface=str(self.clidict.interface))
        self.sniffer.start()
        self.displaythreading = DisplayPacket(self.sniff_queue, self.ui.packet_list)
        self.displaythreading.start()
        self.ui.action_stop.setEnabled(True)

    def stop_sniffer(self):
        self.sniffer.terminate()

        self.sniff_queue.close()
        while True:
            if self.sniff_queue.empty():
                break
        self.displaythreading.terminate()

class DisplayPacket(threading.Thread):

    def __init__(self, queue, packet_list, *args, **kwargs):
        super(DisplayPacket, self).__init__(*args, **kwargs)
        self.sniff_queue = queue
        self.packet_list = packet_list
        self._terminate = False
        self._suspend_lock = threading.Lock()
    def suspend(self):
        #self.sniff_queue.join()
        self._suspend_lock.acquire()
    def resume(self):
        self._suspend_lock.release()
    def terminate(self):
        #self.sniff_queue.join()

        self._terminate = True

    def run(self):
        while True:
            if self._terminate:
                break
            self._suspend_lock.acquire()
            self._suspend_lock.release()
            item = self.sniff_queue.get()
            self.packet_list.addItem("src:%-15s dst:%-15s proto:%-6s desc:%-40s"%(item["src"],item['dst'],item['proto'],item['desc']))
            #QtGui.QApplication.processEvents()

#    def get_interface(self, ifname):
#        self.clidict.interface = ifname 
#        print(ifname)
#
#    def get_mode(self, mode_name):
#        self.clidict.mode = mode_name
#        print(mode_name)
#    def get_filter(self):
#        self.clidict.filter = self.ui.lineEdit.text()
#        print(self.ui.lineEdit.text())


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
