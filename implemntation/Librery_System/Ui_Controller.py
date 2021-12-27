from PySide2.QtWidgets import QApplication
from Login_window import LoginWindow
from main_window import MainWindow
from modules.Authentication import Authenticate
import sys
import time

if __name__ == "__main__":
    app = QApplication(sys.argv)
    session= Authenticate()
    login = LoginWindow(session)
    login.show()
    def show():
        print("yup")
    window = MainWindow()

    sys.exit(app.exec_())