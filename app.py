from windwow import Mywindows,QApplication
from PyQt6 import QtCore
import windwow
import sys
if __name__=='__main__':
    app=QApplication(sys.argv)
    win=Mywindows(1920,1080,'XON')
    win.setWindowState(QtCore.Qt.WindowState.WindowMaximized)
    win.show()
    app.exec()
