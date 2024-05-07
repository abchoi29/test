import sys
from PyQt5 import QtWidgets, QtCore, QtGui

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
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
        
        

#UI 디자인
    def MainText(self):
        self.setWindowTitle("악성메일 메일 분석기")

    #Lable로 Text 삽입 
        self.label = QLabel("악성메일 분석",self)
        self.label.setGeometry(QtCore.QRect(10,10,600,50))
        self.label.setAlignment(Qt.AlignCenter)

        font1 = self.label.font()
        font1.setPointSize(20)
        font1.setBold(True)

        self.label.setFont(font1)


    #텍스트 입력받음 (LineEdit())
        self.textbox = QtWidgets.QLineEdit(self)   ###텍스트 입력받음 -> 경로 입력받을 때 사용가능할 듯
        self.textbox.setGeometry(QtCore.QRect(100,75,350,55))
        self.textbox.setObjectName("texxxtbox")
        
        font_textbox = self.textbox.font()
        font_textbox.setPointSize(15)
        self.textbox.setFont(font_textbox)

        # self.textbox.///

        layout = QVBoxLayout()   #label 수직정렬
        layout.addWidget(self.label)
        # self.setLayout(layout)


    def image(self):
    #Gmail logo
        self.gmail = QPixmap('C:/Users/22105296/OneDrive - 대구대학교/CapstoneDesign/pyqt/Gmail.jpg')
        self.gmail = self.gmail.scaledToWidth(200)  ##이미지 크기 조정

        self.label_gmail = QLabel(self)
        self.label_gmail.move(350,100)

        self.label_gmail.resize(300,300)
        self.label_gmail.setPixmap(self.gmail)  #라벨 위에 이미지 넣는 방식
        # self.label1.setContentsMargins(100,100,100,100)

    #Naver mail logo     
        self.naver = QPixmap('C:/Users/22105296/OneDrive - 대구대학교/CapstoneDesign/pyqt/naver logo.PNG')
        # self.naver = self.naver.scaledToHeight(120)
        self.naver = self.naver.scaledToWidth(150)  ##이미지 크기 조정
 

        self.label_naver = QLabel(self)
        self.label_naver.move(110,100)

        self.label_naver.resize(300,300)
        self.label_naver.setPixmap(self.naver)
        # self.label1.setContentsMargins(10,10,1000,1000)


    def Button(self):
        fontb = self.label.font()
        fontb.setPointSize(10)
        fontb.setBold(True)
    #Button '파일 불러오기'
        self.file_btn = QPushButton("불러오기",self)
        self.file_btn.setGeometry(QtCore.QRect(450,75,90,25))
        self.file_btn.clicked.connect(self.callfile)
        self.file_btn.setFont(fontb)
        
    #Button '분석'
        self.anal_btn = QPushButton("분석하기",self)
        self.anal_btn.setGeometry(QtCore.QRect(450,100,90,30))
        self.anal_btn.setFont(fontb)

    #Button Gmail
        self.gmail_btn1 = QPushButton('Gmail EML 파일 추출방법', self)
        self.gmail_btn1.move(350,350)
        self.gmail_btn1.setFixedSize(200,50)
        self.gmail_btn1.clicked.connect(self.call_g_window)
        self.gmail_btn1.setFont(fontb)

    
    #Button Naver
        self.naver_btn1 = QPushButton('네이버 EML 파일 추출방법', self)
        self.naver_btn1.move(90,350)
        self.naver_btn1.setFixedSize(200,50)
        self.naver_btn1.clicked.connect(self.call_n_window)
        self.naver_btn1.setFont(fontb)


    def call_g_window(self):
        # self.close()
        self.new_naver=GmailWindow()
        self.new_naver.show()

    def call_n_window(self):
        # self.close()
        self.new_naver=NaverWindow()
        self.new_naver.show()

    def callfile(self):
        filename=QFileDialog.getOpenFileName()
        path = filename[0]
        print(path)



class GmailWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(500,500)
        self.setWindowTitle("Gmail EML")

        self.mid_title = QLabel(self)
        self.mid_title.setGeometry(10,10,500,25)
        self.mid_title.setText('<Gmail EML 파일 추출 방법>')
        self.mid_title.setFont(QtGui.QFont("맑은 고딕",18))   ##글씨체 한줄 수정
        self.mid_title.setAlignment(Qt.AlignCenter)



class NaverWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1500,800)
        self.setWindowTitle("네이버 EML")
        self.setUI()

    def setUI(self):
        self.naver_title = QLabel(self)
        self.naver_title.setGeometry(10,10,1500,50)
        self.naver_title.setText('<네이버 EML 파일 추출 방법>')
        self.naver_title.setFont(QtGui.QFont("맑은 고딕",30))   ##글씨체 한줄 수정
        self.naver_title.setAlignment(Qt.AlignCenter)

        font1 = self.naver_title.font()
        font1.setBold(True)
        self.naver_title.setFont(font1)



        self.naver_eml = QPixmap("C:/Users/22105296/OneDrive - 대구대학교/CapstoneDesign/pyqt/naver eml.png")
        self.naver_eml.scaledToWidth(1500)
       
        self.lable_eml = QLabel(self)
        self.lable_eml.setPixmap(self.naver_eml)
        self.lable_eml.setGeometry(0,90,1500,600)
        self.lable_eml.setAlignment(Qt.AlignCenter)

        self.naver_exp = QLabel(self)
        self.naver_exp.setGeometry(20,730,1500,30)
        self.naver_exp.setText('▷ 수신 메일 클릭 → [더보기] → [PC에 저장하기] → 다운 EML파일 확인')
        self.naver_exp.setFont(QtGui.QFont("맑은 고딕",20))   ##글씨체 한줄 수정
        # self.naver_exp.setAlignment(Qt.AlignCenter)
        

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


