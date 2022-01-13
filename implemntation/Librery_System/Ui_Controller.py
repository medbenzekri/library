from PySide2.QtWidgets import QApplication
from Login_window import LoginWindow
from main_window import MainWindow
import sys


class UI_Controller:
    def __init__(self) -> None:
        self.login = LoginWindow(self)
        self.window = MainWindow()
        self.login.show()

    def success_login(self):
        self.login.close()
        self.window.username = self.login.username
        self.window.show_books()
        self.window.show()
        self.window.message.success("Login Successfully")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = UI_Controller()

    sys.exit(app.exec_())
