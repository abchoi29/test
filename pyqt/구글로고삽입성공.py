import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class test(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        self.lbl.resize(500,500)


        pixmap = QPixmap("C:/Users/22105296/OneDrive - 대구대학교/PyQt Tutorial/hello pyqt/Google logo.png")
        pixmap=pixmap.scaledToWidth(500)


        self.lbl.setPixmap(QPixmap(pixmap))
        
        self.resize(1000,1000)
        self.show()

app = QApplication(sys.argv)
test = test()
sys.exit(app.exec_())