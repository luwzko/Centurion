import sys
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QPlainTextEdit, QPushButton, QWidget, QLabel
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt, pyqtSignal
from server import Server

class Control_Panel(Server, QWidget):

    def __init__(self):
        super(Control_Panel, self).__init__()

        self.title = "Centurion " + "v1.0 Beta"
        self.w = 950
        self.h = 700
        self.app = QApplication(sys.argv)
        self.widget = QWidget()
        self.server = Server()
        self.widget.keyPressEvent = self.keyPressEvent
        
        self.ui()

    def ui(self):

        self.console()
                          #(x , y) (window size)
        self.widget.setFixedSize(self.w, self.h)
        self.widget.setWindowTitle(self.title)
        self.widget.show()

        sys.exit(self.app.exec_())
    
    def console(self):
        
        self.consoleentry = QLineEdit(self.widget)
        self.consoleentry.move(5, self.h-30)
        self.consoleentry.resize(self.w-10, 25)

        self.consoleoutput = QPlainTextEdit(self.widget)
        self.consoleoutput.move(5, self.h-200)
        self.consoleoutput.resize(self.w-10, 170)
        self.consoleoutput.setReadOnly(True)

    def keyPressEvent(self, e : QKeyEvent):
        if e.key() == Qt.Key_Return:
            resp = self.server.send_and_recv(self.consoleentry.text())
            self.consoleoutput.setPlainText(resp)
            self.consoleentry.clear()
        e.accept()
a = Control_Panel()