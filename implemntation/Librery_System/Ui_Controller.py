from PySide2.QtWidgets import QApplication
from Login_window import LoginWindow
from modules.Authentication import Authenticate
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    session= Authenticate()
    login = LoginWindow(session)
    login.show()

    sys.exit(app.exec_())
