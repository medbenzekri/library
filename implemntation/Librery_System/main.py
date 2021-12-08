import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import*
from PySide2.QtSvg import *
from modules.BookCardgui import Card
# GUI FILE
from modules.libgui import Ui_MainWindow

# IMPORT FUNCTIONS
from modules.ui_functions import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        #self.ui = Ui_MainWindow()
        #self.ui.setupUi(self)
        
        # self.ui.menu_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self))
        # self.ui.home_btn.clicked.connect(lambda: self.ui.pages_Widget.setCurrentWidget(self.ui.page_2))
        # self.ui.search_btn.clicked.connect(lambda: self.ui.pages_Widget.setCurrentWidget(self.ui.page_3))
        path="https://m.media-amazon.com/images/I/51p-p9etkTL.jpg"
        babylion={"name":"Lion","author":"some lion","image":path}
        self.card=Card(babylion)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
    
