
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
import json
import os

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.add_note)

        if os.path.exists("bobr.json") and os.path.getsize("bobr.json"):
            with open("bobr.json") as file:
                self.notes = json.load(file)
                self.ui.listWidget.addItems(self.notes.keys())

    def add_note(self):
        text, ok = QInputDialog.getText(self,"Додай замітку", "введіть текст")
        if ok:
            self.ui.listWidget.addItem(text)


        

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()