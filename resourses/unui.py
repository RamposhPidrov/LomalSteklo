import sys
import time
import threading

import main as main
import connection as connection
from switch import SwitchButton
from Extend import *
from PyQt5 import QtCore, QtGui, QtWidgets





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
        global mrglobal
        global Con
        global lock
        global lock2
        while lock2:
            #print('th1')
            d = 'da'
            #print(d)
        lock = True
        ohno = True

        if '' in [self.con.lineEdit.text(), self.con.lineEdit_2.text(), self.con.lineEdit_3.text(), self.con.lineEdit_4.text()]:
            lock = False
            return 0

        try:
            if type(main.Connection(
                '{0}.{1}.{2}.{3}'.format(self.con.lineEdit.text(), self.con.lineEdit_2.text(),
                                         self.con.lineEdit_3.text(),
                                         self.con.lineEdit_4.text()),
                'public', 161).get_interfaces()) is not list:
                print('Invalid host address')
                lock = False
                return 0

        except:
            print('There is no such host')
            lock = False
            return 0
        self.f('{0}.{1}.{2}.{3}'.format(self.con.lineEdit.text(), self.con.lineEdit_2.text(),
                                        self.con.lineEdit_3.text(), self.con.lineEdit_4.text()))
        Connections.append(main.Connection(
            '{0}.{1}.{2}.{3}'.format(self.con.lineEdit.text(), self.con.lineEdit_2.text(),
                                     self.con.lineEdit_3.text(),
                                     self.con.lineEdit_4.text()),
            'public', 161))
        Con.append(['{0}.{1}.{2}.{3}'.format(self.con.lineEdit.text(), self.con.lineEdit_2.text(),
                                                 self.con.lineEdit_3.text(), self.con.lineEdit_4.text()), 'public', 161])

        try:
            self.f3()
        except:
            time.sleep(1)
            self.f3()
        self.f2()
        mrglobal = True
        self.close()
        self.destroy()

    def keyPressEvent(self, e):

        try:
            if e.key() == QtCore.Qt.Key_Enter or e.key() == QtCore.Qt.Key_Return:

                self.con.lineEdit_4.setReadOnly(True)
                self.con.lineEdit_3.setReadOnly(True)
                self.con.lineEdit_2.setReadOnly(True)
                self.con.lineEdit.setReadOnly(True)
                self.con.pushButton.click()
        except:
            da = 'da'
            #self.submit()


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

    def start_background_job(self):
        # No harm in calling thread.start() after the thread is already started.
        self.thread.start()
        self.signal_start_background_job.emit()





    def info(self):
        self.ui.clear()
        global lock
        global lock2
        global Connections
        global Con
        #print(Connections)
        k = 0
        for i in self.ui.ConList:

           # print( i.dict['int'])
            #i.clearInt()
            #i.Interfaces.clear()
            #print(len(Connections[k]))
            int = Connections[k].get_interfaces()
            if len(int) > len(i.Interfaces):
                for j in range(0, len(int)):

                    i.AddInt()
            q = 0
            self.MyFunction(i.dict['switch'])
            info = [Connections[k].get_systeminfo(), Connections[k].get_uptime()]
            i.dict['label'].setText('{0}\n{1}'.format(info[0], info[1]))
            try:

                for j in i.Interfaces:
                    parohod = []
                    another = True
                    while another:
                        try:
                            parohod = [int[q][3], int[q][4], int[q][1], int[q][2], int[q][8], int[q][10], int[q][16]]
                            
                            another = False
                        except:
                            time.sleep(0.1)
                            continue
                    j.d['name'].setText(parohod[0])

                    if (parohod[1]) == 'up':
                        j.d['logo'].setPixmap(QtGui.QPixmap("resourses/images/recGr.png"))
                    else:
                        j.d['logo'].setPixmap(QtGui.QPixmap("resourses/images/recRed.png"))
                    try:
                        j.d['text'].setPlainText('IPADDRESS {0:<10}\nNETMASK    {1:<10}\nMAC     {2:<10}\nBYTES RECEIVED  {3}\nBYTES SENT          {4}'.format(parohod[2], parohod[3], parohod[4], parohod[5], parohod[6]))
                    except:
                        j.d['text'].setPlainText('error')
                    q += 1
            except:
                print('MLYA YA MASLINU POIMAL')


            i.dict['groupBox'].setWhatsThis('{0}'.format(len(i.Interfaces)))
            self.MyFunction(i.dict['switch'])
            k += 1
        lock = False

    def smart(self, j, Connections):
        j.d['name'].setText(Connections[3])
        j.d['text'].setPlainText('IPADDRESS {0:<10}\nNETMASK    {1:<10}'.format(Connections[1], Connections[2]))


    def MyFunction(self, master):
        if not mrglobal:
            d = {True: 60 + 210 * int(master.parent().whatsThis()), False: 70}
            bool = master._value
            master.parent().setMinimumSize(QtCore.QSize(16777215, d[bool]))
            master.parent().setMaximumSize(QtCore.QSize(16777215, d[bool]))
            master.parent().children()[list(map(lambda x: str(x).find('QFrame'), master.parent().children())).index(17)].setVisible(bool)
        else:
            master.setValue(True)

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
        #print('g')
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
        global mrglobal
        global lock
        global Connections
        global Con
        global lock2
        while True:
            b = 0
            while lock:

                if not lock2:
                    lock = False
                #print(lock2)
                da = 'da'
            lock2 = True
            for i in range(0, len(Connections)):
                try:
                    #print(Connections[i])
                    Connections[i] = main.Connection(Con[i][0],Con[i][1], Con[i][2])
                    #print(Connections[i])
                except:
                    print('PAPA', Connections)
                    #Con = Con[:-1]
                    #Connections = Connections[:-1]
                    break
                b = i

            delegate()

           # print('ddd')

            qwer += 1
            lock2 = False
            mrglobal = False
            time.sleep(5)

            pass


if __name__=="__main__":
    qwer = 0
    delegate = None
    mrglobal = False
    lock = False
    lock2 = False
    Con = []
    Connections = []
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
