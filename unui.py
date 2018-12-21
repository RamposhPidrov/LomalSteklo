import sys
import time
import threading

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
    signal_start_background_job = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        global delegate
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.EventBound()
        self.ui.action.triggered.connect(self.NewConnection)
        self.ui.action_3.triggered.connect(self.DeleteConnection)
        self.Mem = []

        delegate = self.info
        self.worker = WorkerObject()
        self.thread = QtCore.QThread()
        self.worker.moveToThread(self.thread)

        self.signal_start_background_job.connect(self.worker.background_job)
        self.start_background_job()
        #self.ui.action.toggled.connect(self.NewLog)  # .changed().connect()
        #self.ui.switch1.clicked(self.MyFunction)
       # self.ui.switch1_2.clicked(self.MyFunction)
        #self.ui.switch1_3.clicked(self.MyFunction)
        #self.ui.pushButton.clicked.connect()

    def start_background_job(self):
        # No harm in calling thread.start() after the thread is already started.
        self.thread.start()
        self.signal_start_background_job.emit()





    def info(self):
        self.ui.clear()

        global Connections
        print(Connections)
        k = 0
        for i in self.ui.ConList:

           # print( i.dict['int'])
            #i.clearInt()
            #i.Interfaces.clear()
            #print(len(Connections[k]))
            if len(Connections[k]) > len(i.Interfaces):
                for j in range(0, len(Connections[k])):

                    i.AddInt()
            q = 0
            for j in i.Interfaces:
                print((Connections[k][q][3]))
                j.d['name'].setText(Connections[k][q][3])
                j.d['text'].setPlainText('IPADDRESS {0:<10}\nNETMASK    {1:<10}\n{2}'.format(Connections[k][q][1], Connections[k][q][2], qwer))
                q += 1

            i.dict['groupBox'].setWhatsThis('{0}'.format(len(i.Interfaces)))
            k += 1

    def smart(self, j, Connections):
        j.d['name'].setText(Connections[3])
        j.d['text'].setPlainText('IPADDRESS {0:<10}\nNETMASK    {1:<10}'.format(Connections[1], Connections[2]))


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

class WorkerObject(QtCore.QObject):
    @QtCore.pyqtSlot()
    def background_job(self):
        global qwer
        while True:
            delegate()
            print('ddd')
            qwer += 1
            time.sleep(5)
            pass


if __name__=="__main__":
    qwer = 0
    delegate = None
    Connections = []
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())