# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\qtuer\Desktop\Kursach\LomalSteklo\mw.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    class dd:
        def __init__(self, centralwidget, verticalLayout, i):
            self.groupBox = QtWidgets.QGroupBox(centralwidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
            self.groupBox.setSizePolicy(sizePolicy)
            self.groupBox.setMinimumSize(QtCore.QSize(0, 100))
            self.groupBox.setMaximumSize(QtCore.QSize(16777215, 100))
            self.groupBox.setObjectName("groupBox{0}".format(i))
            self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
            self.gridLayout.setObjectName("gridLayout{0}".format(i))
            self.switch1 = SwitchButton(self.groupBox)
            self.switch1.setMinimumSize(QtCore.QSize(70, 25))
            self.switch1.setMaximumSize(QtCore.QSize(16777215, 25))
            self.switch1.setToolTipDuration(-1)
            self.switch1.setAutoFillBackground(False)
            self.switch1.setObjectName("switch1{0}".format(i))
            self.gridLayout.addWidget(self.switch1, 0, 1, 1, 1)
            spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
            self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
            spacerItem1 = QtWidgets.QSpacerItem(797, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
            spacerItem2 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum,
                                                QtWidgets.QSizePolicy.MinimumExpanding)
            self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
            self.inFrame = QtWidgets.QFrame(self.groupBox)
            self.inFrame.setEnabled(True)
            self.inFrame.setMinimumSize(QtCore.QSize(0, 200))
            self.inFrame.setAutoFillBackground(False)
            # self.inFrame.setStyleSheet("backgroundcolor: rgb(93, 78, 255)")
            self.inFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.inFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.inFrame.setObjectName("inFrame{0}".format(i))
            self.label_2 = QtWidgets.QLabel(self.inFrame)
            self.label_2.setGeometry(QtCore.QRect(170, 30, 221, 61))
            self.label_2.setObjectName("label_2{0}".format(i))
            self.gridLayout.addWidget(self.inFrame, 2, 0, 1, 1)
            verticalLayout.addWidget(self.groupBox)
            spacerItem3 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
            verticalLayout.addItem(spacerItem3)

            self.dict = {
                'groupBox': self.groupBox,
                'switch': self.switch1
            }

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1193, 728)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.LogList = []
        self.LogList.append(self.dd(self.centralwidget, self.verticalLayout, len(self.LogList)))

        '''
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.switch1 = SwitchButton(self.groupBox)
        self.switch1.setMinimumSize(QtCore.QSize(70, 25))
        self.switch1.setMaximumSize(QtCore.QSize(16777215, 25))
        self.switch1.setToolTipDuration(-1)
        self.switch1.setAutoFillBackground(False)
        self.switch1.setObjectName("switch1")
        self.gridLayout.addWidget(self.switch1, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(797, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.inFrame = QtWidgets.QFrame(self.groupBox)
        self.inFrame.setEnabled(True)
        self.inFrame.setMinimumSize(QtCore.QSize(0, 200))
        self.inFrame.setAutoFillBackground(False)
        self.inFrame.setStyleSheet("backgroundcolor: rgb(93, 78, 255)")
        self.inFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inFrame.setObjectName("inFrame")
        self.label_2 = QtWidgets.QLabel(self.inFrame)
        self.label_2.setGeometry(QtCore.QRect(170, 30, 221, 61))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.inFrame, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem3 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem3)


        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.switch1_2 = SwitchButton(self.groupBox_2)
        self.switch1_2.setMinimumSize(QtCore.QSize(70, 25))
        self.switch1_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.switch1_2.setToolTipDuration(-1)
        self.switch1_2.setAutoFillBackground(False)
        self.switch1_2.setObjectName("switch1_2")
        self.gridLayout_2.addWidget(self.switch1_2, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_2.addItem(spacerItem5, 1, 0, 1, 1)
        self.inFrame_2 = QtWidgets.QFrame(self.groupBox_2)
        self.inFrame_2.setEnabled(True)
        self.inFrame_2.setMinimumSize(QtCore.QSize(0, 200))
        self.inFrame_2.setAutoFillBackground(False)
        self.inFrame_2.setStyleSheet("backgroundcolor: rgb(93, 78, 255)")
        self.inFrame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inFrame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inFrame_2.setObjectName("inFrame_2")
        self.label_3 = QtWidgets.QLabel(self.inFrame_2)
        self.label_3.setGeometry(QtCore.QRect(170, 30, 221, 61))
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.inFrame_2, 2, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(797, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem7)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.switch1_3 = SwitchButton(self.groupBox_3)
        self.switch1_3.setMinimumSize(QtCore.QSize(70, 25))
        self.switch1_3.setMaximumSize(QtCore.QSize(16777215, 25))
        self.switch1_3.setToolTipDuration(-1)
        self.switch1_3.setAutoFillBackground(False)
        self.switch1_3.setObjectName("switch1_3")
        self.gridLayout_3.addWidget(self.switch1_3, 0, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 0, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_3.addItem(spacerItem9, 1, 0, 1, 1)
        self.inFrame_3 = QtWidgets.QFrame(self.groupBox_3)
        self.inFrame_3.setEnabled(True)
        self.inFrame_3.setMinimumSize(QtCore.QSize(0, 200))
        self.inFrame_3.setAutoFillBackground(False)
        self.inFrame_3.setStyleSheet("backgroundcolor: rgb(93, 78, 255)")
        self.inFrame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inFrame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inFrame_3.setObjectName("inFrame_3")
        self.label_4 = QtWidgets.QLabel(self.inFrame_3)
        self.label_4.setGeometry(QtCore.QRect(170, 30, 221, 61))
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.inFrame_3, 2, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(797, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem10, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        '''
        spacerItem11 = QtWidgets.QSpacerItem(20, 288, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem11)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1193, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.menu_2.addAction(self.action)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        # self.label_2.setText(_translate("MainWindow", "Ну и помойка"))
        # self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        # self.label_3.setText(_translate("MainWindow", "Ну и помойка"))
        # self.groupBox_3.setTitle(_translate("MainWindow", "GroupBox"))
        # self.label_4.setText(_translate("MainWindow", "Ну и помойка"))
        self.label.setText(_translate("MainWindow", "Copyright Petrovich.inc"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Соединение"))
        self.action.setText(_translate("MainWindow", "Добавить"))
        self.action_3.setText(_translate("MainWindow", "Удалить"))

    def createLog(self):
        self.LogList.append(self.dd(self.MainWindow, self.centralwidget, self.verticalLayout, len(self.LogList)))


from switch import SwitchButton
