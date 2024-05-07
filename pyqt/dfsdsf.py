import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


# class QPushButton(QPushButton):
#     def __init__(self, parent = None):

class mywindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,300,300,300)
        self.setWindowIcon(QIcon(""))
        self.initUI()




       

        

#UI 디자인
    def initUI(self):
        self.setWindowTitle("탐지 프로그램")

    #Text 삽입 
        self.LabelTitle = QLabel(self)
        self.LabelTitle.setGeometry(10,10,500,25)
        self.LabelTitle.setText('악성메일 탐지프로그램 - eml 파일 추출방법 설명')


app = QApplication(sys.argv)
window = mywindow()
label = QLabel()

window.show()
app.exec_()
