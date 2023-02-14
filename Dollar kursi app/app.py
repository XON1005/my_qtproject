from Data.main import Mainkurs, QApplication, QtCore
import sys
if __name__=="__main__":
    app= QApplication(sys.argv)
    win=Mainkurs(1920,1080,"KURS")
    win.setWindowState(QtCore.Qt.WindowState.WindowMaximized)
    style = """
    background: url('Img/7680x4320-neon-green-solid-color-background.png');
    """
    win.setStyleSheet(style)
    win.show()
    app.exec()