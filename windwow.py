from PyQt6.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton,QTextEdit
from PyQt6 import QtCore
from PyQt6.QtGui import QIcon
class Mywindows(QMainWindow):
    def __init__(self,width=1920, height=1080, title="QT") -> None:
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(0,0, width, height)
        self.main_btn=QPushButton(QIcon("img\\40-408496_transparent-batman-logo-png-dark-knight-batman-batarang.png"),"XON",self)
        self.main_lbl= QLabel("<b> BU tugma</b>",self)
        self.main_btn.setGeometry(width//2-30,height//2-55,100,100)
        self.main_btn.adjustSize()
        self.main_lbl.setGeometry(width//2-20,height//3+80,100,100)
        self.main_lbl.adjustSize()
        self.main_btn.clicked.connect(self.change_label_text)
    def change_label_text(self):
        self.main_lbl.setText("<b> XON</b>")