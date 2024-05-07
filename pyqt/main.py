import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



# class QPushButton(QPushButton):
#     def __init__(self, parent = None):


class mywindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(1500,300,650,500)
        self.setWindowIcon(QIcon(""))
        self.MainText()
        self.image()
        self.Button()
        self.MainText()
        

#UI 디자인
    def MainText(self):
        global file
        self.setWindowTitle("Find Malicious Email")

    #Text 삽입 
        self.LabelTitle = QLabel(self)
        self.LabelTitle.setGeometry(10,10,500,25)
        self.LabelTitle.setText('Finding Malicious Email')

    def image(self):
    #Gmail logo
        self.gmail = QPixmap('C:/Users/22105296/OneDrive - 대구대학교/CapstoneDesign/pyqt/Gmail.jpg')
        self.gmail = self.gmail.scaledToWidth(200)  ##이미지 크기 조정

        self.label_gmail = QLabel(self)
        self.label_gmail.move(80,0)

        self.label_gmail.resize(300,300)
        self.label_gmail.setPixmap(self.gmail)  #라벨 위에 이미지 넣는 방식
        # self.label1.setContentsMargins(100,100,100,100)

    #Naver mail logo     
        self.naver = QPixmap('C:/Users/22105296/OneDrive - 대구대학교/CapstoneDesign/pyqt/naver logo.PNG')
        self.naver = self.naver.scaledToWidth(150)  ##이미지 크기 조정

        self.label_naver = QLabel(self)
        self.label_naver.move(110,200)

        self.label_naver.resize(300,300)
        self.label_naver.setPixmap(self.naver)
        # self.label1.setContentsMargins(10,10,1000,1000)


    def Button(self):
    #Button Gmail
        self.gmail_btn1 = QPushButton('How to het EML file from Gmail?', self)
        self.gmail_btn1.move(300,100)
        self.gmail_btn1.setFixedSize(200,50)

        self.gmail_btn2 = QPushButton('Analyze Google mail', self)
        self.gmail_btn2.move(300,170)
        self.gmail_btn2.setFixedSize(200,50)

        

    #Button Naver
        self.naver_btn1 = QPushButton('How to get EML file from Naver?', self)
        self.naver_btn1.move(300,300)
        self.naver_btn1.setFixedSize(200,50)
        self.naver_btn1.clicked.connect(self.callwindow)



        self.naver_btn2 = QPushButton('Analyze Naver mail', self)
        self.naver_btn2.move(300,370)
        self.naver_btn2.setFixedSize(200,50)
        self.naver_btn2.clicked.connect(self.callfile)



    def callwindow(self):
        # self.close()
        self.w=NaverWindow()
        self.w.show()

    def callfile(self):
        filename=QFileDialog.getOpenFileName()
        path = filename[0]
        print(path)





class NaverWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(500,500)
        self.setWindowTitle("How to get Naver EML file")

        self.ww = QLabel(self)
        self.ww.setGeometry(10,10,500,25)
        self.ww.setText('Finding Malicious Email')
       

        # self.analyze_dialog = QDialog()
        # self.analyze_dialog.resize(500,300)
        

        # self.analyze_dialog.show()


        # layout = QVBoxLayout()
        # layout.addWidget(self.label1)
        # layout.addWidget(self.label2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mywindow()
    label = QLabel()

    window.show()
    app.exec_()  #앱이랑 ui 연결


