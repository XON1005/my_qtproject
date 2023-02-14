from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QTextEdit,QButtonGroup
from PyQt6 import QtCore
from PyQt6.QtGui import QIcon
from Data.getkurs import get_kur
class Mainkurs(QMainWindow):
    def __init__(self, width=500, height=500,title="Kurs App"):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(500,250,width,height)
        icon_title= QIcon("Img/money-bag.png")
        far_icon= QIcon("Img/dollar-symbol.png") #ikonka tanlash uchun
        self.setWindowIcon(icon_title) #ikonka qoyish uchun
        self.sbutton= QLabel(" = ",self)
        self.sbutton.setGeometry(width//14+120,125,20,10)
        self.fbutton = QPushButton(far_icon,"Kursni ko'rish",self) #tugmaga ikon, va nom berish uchun
        self.fbutton.setGeometry(width//15,100,110,60) #tugma joylashuvini belgilash uchun
        self.kurss=QLabel("Kurs",self)
        self.kurss.setGeometry(290,70,350,120)
        self.fbutton.clicked.connect(self.dollar_kurs)
        style= """
    background: no-repeat url('Img/1612648724_135-p-oboi-zelenii-fon-na-android-162.jpg');
    """

    def dollar_kurs(self):
        kurs= get_kur("Bank")
        print(kurs)
        print(type(kurs))
        self.kurss.setText(kurs)