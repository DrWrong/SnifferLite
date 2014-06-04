# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'snifferlite.ui'
#
# Created: Wed May  7 19:51:11 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(849, 540)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 591, 301))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 589, 299))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.packet_list = QtGui.QListWidget(self.scrollAreaWidgetContents)
        self.packet_list.setGeometry(QtCore.QRect(10, 10, 571, 271))
        self.packet_list.setObjectName(_fromUtf8("packet_list"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 849, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidget_3 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_3.setMinimumSize(QtCore.QSize(105, 42))
        self.dockWidget_3.setObjectName(_fromUtf8("dockWidget_3"))
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName(_fromUtf8("dockWidgetContents_3"))
        self.verticalLayoutWidget = QtGui.QWidget(self.dockWidgetContents_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 231, 241))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.interface_choice = QtGui.QComboBox(self.verticalLayoutWidget)
        self.interface_choice.setObjectName(_fromUtf8("interface_choice"))
        self.verticalLayout.addWidget(self.interface_choice)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.mode_choice = QtGui.QComboBox(self.verticalLayoutWidget)
        self.mode_choice.setObjectName(_fromUtf8("mode_choice"))
        self.mode_choice.addItem(_fromUtf8(""))
        self.mode_choice.addItem(_fromUtf8(""))
        self.mode_choice.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.mode_choice)
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.start = QtGui.QPushButton(self.verticalLayoutWidget)
        self.start.setObjectName(_fromUtf8("start"))
        self.verticalLayout.addWidget(self.start)
        self.label_3 = QtGui.QLabel(self.dockWidgetContents_3)
        self.label_3.setGeometry(QtCore.QRect(92, 136, 20, 20))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.dockWidget_3.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_3)
        self.dockWidget_4 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_4.setObjectName(_fromUtf8("dockWidget_4"))
        self.dockWidgetContents_4 = QtGui.QWidget()
        self.dockWidgetContents_4.setObjectName(_fromUtf8("dockWidgetContents_4"))
        self.packet_details = QtGui.QTextBrowser(self.dockWidgetContents_4)
        self.packet_details.setGeometry(QtCore.QRect(10, 10, 831, 192))
        self.packet_details.setObjectName(_fromUtf8("packet_details"))
        self.verticalScrollBar = QtGui.QScrollBar(self.dockWidgetContents_4)
        self.verticalScrollBar.setGeometry(QtCore.QRect(820, 20, 16, 160))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName(_fromUtf8("verticalScrollBar"))
        self.dockWidget_4.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget_4)
        self.action_start = QtGui.QAction(MainWindow)
        self.action_start.setEnabled(False)
        self.action_start.setObjectName(_fromUtf8("action_start"))
        self.action_pause = QtGui.QAction(MainWindow)
        self.action_pause.setEnabled(False)
        self.action_pause.setObjectName(_fromUtf8("action_pause"))
        self.action_stop = QtGui.QAction(MainWindow)
        self.action_stop.setEnabled(False)
        self.action_stop.setObjectName(_fromUtf8("action_stop"))
        self.action_quite = QtGui.QAction(MainWindow)
        self.action_quite.setObjectName(_fromUtf8("action_quite"))
        self.menu.addAction(self.action_quite)
        self.menubar.addAction(self.menu.menuAction())
        self.toolBar.addAction(self.action_start)
        self.toolBar.addAction(self.action_pause)
        self.toolBar.addAction(self.action_stop)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "SnifferLite", None))
        self.menu.setTitle(_translate("MainWindow", "文件", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.label.setText(_translate("MainWindow", "选择网卡", None))
        self.label_2.setText(_translate("MainWindow", "嗅探模式", None))
        self.mode_choice.setItemText(0, _translate("MainWindow", "negtive", None))
        self.mode_choice.setItemText(1, _translate("MainWindow", "arp_mode", None))
        self.mode_choice.setItemText(2, _translate("MainWindow", "mac_flood_mode", None))
        self.label_4.setText(_translate("MainWindow", "Filter", None))
        self.start.setText(_translate("MainWindow", " 开始", None))
        self.action_start.setText(_translate("MainWindow", "开始", None))
        self.action_pause.setText(_translate("MainWindow", "暂停", None))
        self.action_stop.setText(_translate("MainWindow", "停止", None))
        self.action_quite.setText(_translate("MainWindow", "退出", None))

