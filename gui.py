#! /usr/bin/env python
# coding:utf-8
import sys
from PyQt4 import QtGui, QtCore
from ui import Ui_MainWindow
from sniffer import SnifferProcess
import multiprocessing
import netifaces
import logging
from Queue import Queue
from cli import sniffer_prepare
logging.basicConfig(
    filename="snifferlite.log",
    format="%(levelname)-10s %(asctime)s %(message)s",
    level=logging.DEBUG
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
#        QtCore.QObject.connect(
#            self.ui.interface_choice, QtCore.SIGNAL("activated(const QString&)"), self.get_interface)
#
#        QtCore.QObject.connect(
#            self.ui.mode_choice, QtCore.SIGNAL("activated(const QString&)"), self.get_mode)
#        QtCore.QObject.connect(
# self.ui.lineEdit, QtCore.SIGNAL("editingFinished()"), self.get_filter)

    def start_sniffer(self):
        self.clidict.interface = str(self.ui.interface_choice.currentText())
        self.clidict.mode = str(self.ui.mode_choice.currentText())
        self.clidict.filter = str(self.ui.lineEdit.text())
        log.debug(self.clidict.interface + '' +
                  self.clidict.mode + '' + self.clidict.filter)
        sniffer_prepare(self.clidict)
        self.sniff_queue = Queue()
        sniffer = SnifferProcess(
            self.sniff_queue, iface=self.clidict.interface)
        sniffer.start()
        while True:
            item = self.sniff_queue.get()

            self.ui.packet_list.addItem(item.summary())
            QtGui.QApplication.processEvents()

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


def start_gui():
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    start_gui()
