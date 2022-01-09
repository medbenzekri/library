

import sys
from PySide2.QtWidgets import QApplication
from modules.Authentication import Authenticate
from main_window import MainWindow

if __name__=="__main__":
    app = QApplication(sys.argv)
    Authenticate()
    w=MainWindow()
    w.show()
    sys.exit(app.exec_())


