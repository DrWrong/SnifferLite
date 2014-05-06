#! /usr/bin/env python
# coding:utf-8
import sys
from PyQt4 import QtGui, QtCore
from ui import Ui_MainWindow
from sniffer import SnifferProcess
import multiprocessing



class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.start, QtCore.SIGNAL("clicked()"), self.start_sniffer)

    def start_sniffer(self):
        self.sniff_queue = multiprocessing.JoinableQueue()
        sniffer = SnifferProcess(self.sniff_queue)
        sniffer.start()
        while True:
            item = self.sniff_queue.get()

            self.ui.snifferoutput.addItem(str(item))
            QtGui.QApplication.processEvents()



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())