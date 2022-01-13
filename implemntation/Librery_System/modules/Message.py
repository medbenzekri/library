from PySide2.QtCore import QThread, Signal
from PySide2.QtWidgets import QMainWindow, QPushButton
import time


class myMessage:

    def __init__(self, form: QMainWindow, h=30) -> None:
        form.button = QPushButton(form)
        form.button.setGeometry(0, form.height(), form.width(), h)

        self.form = form
        self.button = form.button
        self.message = myThread(h)
        self.h = h

    def success(self, text: str) -> None:
        self.button.setText(text)
        self.button.setStyleSheet(
            u"QPushButton{\n""	color: rgb(255, 255, 255);\n""	background-color: rgb(17, 255, 17);\n""border: none;\n""}")

        self.__run()

    def error(self, text: str) -> None:
        self.button.setText(text)
        self.button.setStyleSheet(
            u"QPushButton{\n""	color: rgb(255, 255, 255);\n""	background-color: rgb(255, 17, 17);\n""border: none;\n""}")

        self.__run()

    def setHeigth(self, h: int) -> None:
        self.h = h

    def __run(self):
        if (self.message.isRunning()):
            self.button.setGeometry(0, self.form.height(), self.button.width(), self.h)
            self.message.terminate()

        self.message = myThread(self.h)

        self.message.start()
        self.message.update_y.connect(self.call_update_y)

    def call_update_y(self, y):
        self.button.setGeometry(0, self.button.y() + y, self.button.width(), self.h)


class myThread(QThread):
    update_y = Signal(int)

    def __init__(self, x: int, parent=None):
        super(myThread, self).__init__(parent)
        self.x = x

    def run(self):
        for i in range(self.x):
            self.update_y.emit(-1)
            time.sleep(0.4 / self.x)

        time.sleep(2)

        for i in range(self.x):
            self.update_y.emit(1)
            time.sleep(1 / self.x)
