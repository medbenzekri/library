from modules.Authentication import Authenticate
from modules.login_gui import Ui_form
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtCore import Qt
from modules.Authentication import Authenticate
import sys

class LoginWindow(QMainWindow, Ui_form):

    def __init__(self,controller,parent = None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda:self.login(controller))
        
    def login(self,controller) -> None:
        if Authenticate.login(self.username.text(),self.password.text()):
            controller.success_login()
        else:
            self.message.error("Login Faild")  
      
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = LoginWindow()
    myWin.show()
    sys.exit(app.exec_())
