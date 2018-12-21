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
            self.Interfaces = []

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
            self.pushButton2 = QtWidgets.QPushButton(self.groupBox)
            self.pushButton2.setStyleSheet("background-image: url(:/images/garbage_red.png);")
            self.pushButton2.setText("")
            self.pushButton2.setObjectName("pushButton2")
            self.pushButton2.setIcon(QtGui.QIcon("images/garbage_red.png"))
            self.switch1 = SwitchButton(self.groupBox)
            self.switch1.setMinimumSize(QtCore.QSize(70, 25))
            self.switch1.setMaximumSize(QtCore.QSize(16777215, 25))
            self.switch1.setToolTipDuration(-1)
            self.switch1.setAutoFillBackground(False)
            self.switch1.setObjectName("switch1{0}".format(i))
            self.gridLayout.addWidget(self.switch1, 0, 1, 1, 1)
            self.gridLayout.addWidget(self.pushButton2, 0, 4, 4, 4)
            spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
            self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
            spacerItem1 = QtWidgets.QSpacerItem(797, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
            spacerItem2 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum,
                                                QtWidgets.QSizePolicy.MinimumExpanding)
            self.gridLayout.addItem(spacerItem2, 4, 0, 1, 1)
            self.inFrame = QtWidgets.QFrame(self.groupBox)
            self.inFrame.setEnabled(True)
            self.inFrame.setMinimumSize(QtCore.QSize(0, 200))
            self.inFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
            self.inFrame.setAutoFillBackground(False)
            # self.inFrame.setStyleSheet("backgroundcolor: rgb(93, 78, 255)")
            self.inFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.inFrame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.inFrame.setObjectName("inFrame{0}".format(i))

            self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.inFrame)
            self.verticalLayout_3.setObjectName("verticalLayout_3")
            spacerItem6 = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
            self.verticalLayout_3.addItem(spacerItem6)

            #self.Interfaces.append(self.Interface(self.inFrame, self.verticalLayout_3))
            #self.Interfaces.append(self.Interface(self.inFrame, self.verticalLayout_3))

            #self.Interfaces.append(self.Interface(self.inFrame, self.verticalLayout_3))

            spacerItem8 = QtWidgets.QSpacerItem(20, 163, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.verticalLayout_3.addItem(spacerItem8)
            self.gridLayout.addWidget(self.inFrame, 2, 0, 1, 1)

            #self.gridLayout.addWidget(self.inFrame, 2, 0, 1, 1)
            verticalLayout.addWidget(self.groupBox)
            spacerItem3 = QtWidgets.QSpacerItem(10, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
            verticalLayout.addItem(spacerItem3)
            self.groupBox.setWhatsThis('{}'.format(len(self.Interfaces)))

            self.dict = {
                'groupBox': self.groupBox,
                'switch': self.switch1,
                #'text': self.intName,
                'delete': self.pushButton2,
                'intCount': 0,
                'isDeleted': False,
                'int': self.Interfaces,

            }

            self.pushButton2.clicked.connect(self.DeleteConnection)

        def DeleteConnection(self):
            self.dict['groupBox'].setVisible(False)
            self.dict['isDeleted'] = True

        def AddInt(self):
            self.Interfaces.append(self.Interface(self.inFrame, self.verticalLayout_3))
            print(self.Interfaces)

        def clearInt(self):
            for i in self.Interfaces:
                i.delete()

        class Interface:
            def __init__(self, Frame, layout):
                self.frame = QtWidgets.QFrame(Frame)
                self.frame.setMinimumSize(QtCore.QSize(0, 190))
                self.frame.setMaximumSize(QtCore.QSize(16777215, 200))
                self.frame.setFrameShape(QtWidgets.QFrame.Box)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
                self.gridLayout_4.setObjectName("gridLayout_4")
                self.label_2 = QtWidgets.QLabel(self.frame)
                self.label_2.setText("")
                self.label_2.setTextFormat(QtCore.Qt.AutoText)
                self.label_2.setPixmap(QtGui.QPixmap("images/garbage_red.png"))
                self.label_2.setObjectName("label_2")
                self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
                self.intName = QtWidgets.QLabel(self.frame)
                self.intName.setObjectName("intName")
                self.gridLayout_4.addWidget(self.intName, 0, 1, 1, 1)
                self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame)
                self.plainTextEdit.setInputMethodHints(QtCore.Qt.ImhMultiLine)
                self.plainTextEdit.setReadOnly(True)
                self.plainTextEdit.setObjectName("plainTextEdit")
                self.gridLayout_4.addWidget(self.plainTextEdit, 1, 1, 1, 1)

                layout.addWidget(self.frame)
                spacerItem7 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum,
                                                    QtWidgets.QSizePolicy.Maximum)
                layout.addItem(spacerItem7)

                self.d = {
                    'logo': self.label_2,
                    'name': self.intName,
                    'text': self.plainTextEdit
                }

            def delete(self):
                self.frame.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1193, 728)
        #self.WindCopy = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        #self.scrollArea.setMinimumSize(QtCore.QSize(0, 1000))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1635, 1600))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem)





        self.ConList = []
        #self.createConnection()



        self.spacerItem14 = QtWidgets.QSpacerItem(20, 288, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(self.spacerItem14)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum,
                                                  QtWidgets.QSizePolicy.Maximum)

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
        _translate = self._translate
        MainWindow.setWindowTitle(self._translate("MainWindow", "MainWindow"))
        self.label.setText(self._translate("MainWindow", "Copyright Petrovich.inc"))
        self.menu.setTitle(self._translate("MainWindow", "Файл"))
        self.menu_2.setTitle(self._translate("MainWindow", "Соединение"))
        self.action.setText(self._translate("MainWindow", "Добавить"))
        self.action_3.setText(self._translate("MainWindow", "Удалить"))



    def createConnection(self):
        if len(self.ConList) != 0:
            self.verticalLayout_2.removeItem(self.spacerItem14)
            #self.verticalLayout.removeWidget(self.label)
        self.ConList.append(self.dd(self.scrollAreaWidgetContents, self.verticalLayout_2, len(self.ConList)))
        #self.label_2.setText("Ну и помойка")
        #self.ConList[-1].dict['text'].setText('Ну и помойка')
        self.ConList[-1].dict['groupBox'].setTitle('Соединие{0}'.format(len(self.ConList)))
        if len(self.ConList) != 1:
            self.verticalLayout_2.addItem(self.spacerItem14)

    def createCon(self, name):
        if len(self.ConList) != 0:
            self.verticalLayout_2.removeItem(self.spacerItem14)
            #self.verticalLayout.removeWidget(self.label)
        self.ConList.append(self.dd(self.scrollAreaWidgetContents, self.verticalLayout_2, len(self.ConList)))
        #self.label_2.setText("Ну и помойка")
        #self.ConList[-1].dict['text'].setText('Ну и помойка')
        self.ConList[-1].dict['groupBox'].setTitle('{0}'.format(name))
        if len(self.ConList) != 1:
            self.verticalLayout_2.addItem(self.spacerItem14)

    def deleteCon(self, id):
        self.ConList[id].dict['groupBox'].setVisible(False)
        self.ConList.remove(self.ConList[id])


    def deleteConnection(self):
        self.ConList[-1].dict['groupBox'].setVisible(False)
        self.ConList.remove(self.ConList[-1])

    def clear(self):
        for i in self.ConList:
            if i.dict['isDeleted']:
                self.ConList.remove(i)


from switch import SwitchButton
