import sys
# Импортируем наш интерфейс из файла
from Extend import *
#from gui import *
import connection
import main
from PyQt5 import QtCore, QtGui, QtWidgets
from switch import SwitchButton



class ConWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None, func=None, f2=None, f3=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.con = connection.Ui_MainWindow()
        self.con.setupUi(self)
        self.f = func
        self.f2 = f2
        self.f3 = f3
        self.con.pushButton.clicked.connect(self.submit)

    def submit(self):
        global Connections
        self.f('{0}.{1}.{2}.{3}'.format(self.con.lineEdit.text(), self.con.lineEdit_2.text(), self.con.lineEdit_3.text(), self.con.lineEdit_4.text()))



        Connections.append(main.Connection(
            '{0}.{1}.{2}.{3}'.format(self.con.lineEdit.text(), self.con.lineEdit_2.text(), self.con.lineEdit_3.text(), self.con.lineEdit_4.text()),
            'public', 161).get_interfaces())
        self.f3()
        self.f2()
        self.close()
        self.destroy()

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.EventBound()
        self.ui.action.triggered.connect(self.NewConnection)
        self.ui.action_3.triggered.connect(self.DeleteConnection)
        self.Mem = []
        #self.ui.action.toggled.connect(self.NewLog)  # .changed().connect()
        #self.ui.switch1.clicked(self.MyFunction)
       # self.ui.switch1_2.clicked(self.MyFunction)
        #self.ui.switch1_3.clicked(self.MyFunction)
        #self.ui.pushButton.clicked.connect()


    def info(self):
        self.ui.clear()
        global Connections
        print(Connections)
        k = 0
        for i in self.ui.ConList:
           # print( i.dict['int'])
            i.dict['int'] = []
            #print(len(Connections[k]))
            for j in range(0, len(Connections[k])):

                i.AddInt()
            q = 0
            for j in i.Interfaces:

                j.d['name'].setText(Connections[k][q][3])
                q += 1

            i.dict['groupBox'].setWhatsThis('{}'.format(len(i.Interfaces)))
            k += 1


    def MyFunction(self, master):
        d = {True: 60 + 210 * int(master.parent().whatsThis()), False: 60}
        bool = master._value
        master.parent().setMinimumSize(QtCore.QSize(16777215, d[bool]))
        master.parent().setMaximumSize(QtCore.QSize(16777215, d[bool]))
        master.parent().children()[list(map(lambda x: str(x).find('QFrame'), master.parent().children())).index(17)].setVisible(bool)

    def NewConnection(self):

        con = ConWin(func=self.ui.createCon, f2=self.EventBound, f3=self.info)

        self.Mem.append(con)
        self.ui.clear()
        con.show()
        #print(self.ui.ConList)
        #self.ui.createConnection()
        #self.EventBound()

    def DeleteConnection(self):
        self.ui.deleteCon(self.LastBtnId)

    def EventBound(self):
        print('g')
        for i in self.ui.ConList:
            i.dict['switch'].clicked(self.MyFunction)
        try:
            self.MyFunction(self.ui.ConList[-1].dict['switch'])
        except:
            da = 'da'

if __name__=="__main__":
    Connections = []
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())