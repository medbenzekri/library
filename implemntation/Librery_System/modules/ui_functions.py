from PySide2.QtCore import QPropertyAnimation
from PySide2.QtWidgets import QMainWindow

class UIFunctions(QMainWindow):
    max=250
    min=60
    def toggleMenu(self):
        self.animation= QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
        self.animation.setDuration(400)
        self.animation.setStartValue(UIFunctions.min)
        self.animation.setEndValue(UIFunctions.max)
        self.animation.start()
        UIFunctions.max,UIFunctions.min=UIFunctions.min,UIFunctions.max
    def theme(self,file):
        self.setStyleSheet(self.styleSheet()+file)



