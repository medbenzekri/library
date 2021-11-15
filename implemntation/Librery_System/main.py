import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from libgui import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.ui.menu_toggle_btn.clicked.connect(lambda: UIFunctions.toggleMenu(self))

        self.ui.btn_page1.clicked.connect(lambda: self.ui.pages_Widget.setCurrentWidget(self.ui.page_1))

        self.ui.btn_page2.clicked.connect(lambda: self.ui.pages_Widget.setCurrentWidget(self.ui.page_2))

        self.ui.btn_page3.clicked.connect(lambda: self.ui.pages_Widget.setCurrentWidget(self.ui.page_3))

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
    
