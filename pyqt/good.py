import sys
from PyQt5 import QtWidgets, QtCore, QtGui

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *


class mywindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setGeometry(1500,300,650,500)

        self.kkk = QLabel("우준선배\n 명희선배\n 아자아자 파이티잉!!!!!")
        self.kkk.setFont(QtGui.QFont("맑은 고딕",50))
        self.kkk.setGeometry(QtCore.QRect(10,10,700,500))
        self.kkk.setAlignment(Qt.AlignCenter)

        self.kkk.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)    

    window = mywindow()
    label = QLabel()

    window.show()
    app.exec_()