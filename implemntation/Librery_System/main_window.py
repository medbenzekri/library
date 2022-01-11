from PySide2.QtWidgets import QGridLayout, QMainWindow
# GUI FILE
from library.implemntation.Librery_System.modules.BookCardgui import Card
from library.implemntation.Librery_System.modules.DatabaseFetcher import get_books
from library.implemntation.Librery_System.modules.Message import myMessage
from library.implemntation.Librery_System.modules.libgui import Ui_MainWindow
# IMPORT FUNCTIONS
from library.implemntation.Librery_System.modules.ui_functions import UIFunctions


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.menu_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self))
        self.ui.home_btn.clicked.connect(lambda: self.ui.pages_Widget.setCurrentWidget(self.ui.home_page))
        self.ui.search_btn.clicked.connect(lambda: self.ui.pages_Widget.setCurrentWidget(self.ui.search_page))
        self.message = myMessage(self)
        self.books_grid = QGridLayout(self.ui.scrollAreaWidgetContents)
        self.books_grid.setVerticalSpacing(10)
        self.show_books()

    def show_books(self):
        books = get_books(500)
        for i, book in enumerate(books):
            self.books_grid.addWidget(Card(book, self), i // 6, i % 6)
