from PySide2.QtCore import QPropertyAnimation
from main import *

class UIFunctions(MainWindow):
    max=250
    min=70
    def toggleMenu(self):
        self.animation= QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
        self.animation.setDuration(400)
        self.animation.setStartValue(UIFunctions.min)
        self.animation.setEndValue(UIFunctions.max)
        self.animation.start()
        UIFunctions.max,UIFunctions.min=UIFunctions.min,UIFunctions.max


