import sys
# Импортируем наш интерфейс из файла
#from Extend import *
from Extend import *
from PyQt5 import QtCore, QtGui, QtWidgets
from switch import SwitchButton

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.EventBound()
        self.ui.action.triggered.connect(self.NewLog)
        self.ui.action_3.triggered.connect(self.DeleteLog)
        #self.ui.action.toggled.connect(self.NewLog)  # .changed().connect()
        #self.ui.switch1.clicked(self.MyFunction)
       # self.ui.switch1_2.clicked(self.MyFunction)
        #self.ui.switch1_3.clicked(self.MyFunction)
        #self.ui.pushButton.clicked.connect()


    def MyFunction(self, master):
        d = {True: 290, False: 60}
        bool = master._value
        master.parent().setMinimumSize(QtCore.QSize(16777215, d[bool]))
        master.parent().setMaximumSize(QtCore.QSize(16777215, d[bool]))
        master.parent().children()[list(map(lambda x: str(x).find('QFrame'), master.parent().children())).index(17)].setVisible(bool)
        #self.NewLog()
        print('HUI')
        print()

    def NewLog(self):
        self.ui.createLog()
        self.EventBound()

    def DeleteLog(self):
        self.ui.deleteLog()

    def EventBound(self):

        for i in self.ui.LogList:
            i.dict['switch'].clicked(self.MyFunction)

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())