import sys
# Импортируем наш интерфейс из файла
from gui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from switch import SwitchButton

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #print(self.ui.widget._value)
        #self.switchbtn = SwitchButton(self, "On", 15, "Off", 31, 60)

        # Здесь прописываем событие нажатия на кнопку
        #self.ui.pushButton.clicked.connect(self.MyFunction)
        self.ui.switch1.clicked(self.MyFunction)
        self.ui.switch1_2.clicked(self.MyFunction)
        print()
        print(self.ui.switch1.parent().children())


    # Пока пустая функция которая выполняется
    # при нажатии на кнопку
    def MyFunction(self, master):
        d = {True: 290, False: 100}
        print()
        print(self.ui.groupBox)
        # self.ui.groupBox_2.setVisible(not self.ui.groupBox_2.isVisible())
        bool = master._value
        # bool = not self.inFrame.isVisible()
        master.parent().setMaximumSize(QtCore.QSize(16777215, d[bool]))
        master.parent().children()[list(map(lambda x: str(x).find('QFrame'), self.ui.switch1.parent().children())).index(17)].setVisible(bool)


        print('HUI')

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())