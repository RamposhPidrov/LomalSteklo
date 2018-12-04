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
            self.groupBox.setMinimumSize(QtCore.QSize(0, 70))
            self.groupBox.setMaximumSize(QtCore.QSize(16777215, 70))
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
            self.inFrame.setMaximumSize(QtCore.QSize(16777215, 200))
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
            spacerItem3 = QtWidgets.QSpacerItem(10, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
            verticalLayout.addItem(spacerItem3)

            self.dict = {
                'groupBox': self.groupBox,
                'switch': self.switch1,
                'text': self.label_2
            }

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1193, 728)
        #self.WindCopy = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 1000))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1635, 1000))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem)





        self.LogList = []
        self.createLog()



        self.spacerItem14 = QtWidgets.QSpacerItem(20, 288, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(self.spacerItem14)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.spacerItem11 = QtWidgets.QSpacerItem(20, 288, QtWidgets.QSizePolicy.Minimum,
                                                  QtWidgets.QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.spacerItem11)

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
        self._translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(self._translate("MainWindow", "MainWindow"))
        # self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        # self.label_2.setText(_translate("MainWindow", "Ну и помойка"))
        # self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        # self.label_3.setText(_translate("MainWindow", "Ну и помойка"))
        # self.groupBox_3.setTitle(_translate("MainWindow", "GroupBox"))
        # self.label_4.setText(_translate("MainWindow", "Ну и помойка"))
        self.label.setText(self._translate("MainWindow", "Copyright Petrovich.inc"))
        self.menu.setTitle(self._translate("MainWindow", "Файл"))
        self.menu_2.setTitle(self._translate("MainWindow", "Соединение"))
        self.action.setText(self._translate("MainWindow", "Добавить"))
        self.action_3.setText(self._translate("MainWindow", "Удалить"))



    def createLog(self):
        if len(self.LogList) != 0:
            self.verticalLayout_2.removeItem(self.spacerItem14)
            #self.verticalLayout.removeWidget(self.label)
        self.LogList.append(self.dd(self.scrollAreaWidgetContents, self.verticalLayout_2, len(self.LogList)))
        #self.label_2.setText("Ну и помойка")
        self.LogList[-1].dict['text'].setText('Ну и помойка')
        self.LogList[-1].dict['groupBox'].setTitle('Соединие{0}'.format(len(self.LogList)))
        if len(self.LogList) != 1:
            self.verticalLayout_2.addItem(self.spacerItem14)
            #self.verticalLayout.addWidget(self.label)


from switch import SwitchButton
