import csv
from PyQt6.QtWidgets import *
from screeninfo import get_monitors
import sys
from module.transaction import transaction

class MWindow:
    def __init__(self, name):
        self.app = QApplication([])
        self.window = QWidget()
        self.window.setWindowTitle(name)
        self.getScreenSize();
        self.window.setGeometry(0, 0,int(self.width * 0.99), int(self.height * 0.99))
        self.addElements()
        self.window.show()
        sys.exit(self.app.exec())

    def getScreenSize(self):
        self.width = 0
        self.height = 0
        for monitor in get_monitors():
            if monitor.width > self.width:
                self.width = monitor.width
                self.height = monitor.height

    def addElements(self):
        catBtn = QPushButton("categorize",parent=self.window)
        catBtn.setGeometry(int(self.width/3-self.width*0.1),int(self.height*0.05),int(self.width*0.1),int(self.height*0.05))
        catBtn.clicked.connect(self.categorize)
        inputCat = QPlainTextEdit(parent=self.window)
        inputCat.setGeometry(int(self.width/3),int(self.height*0.05),int(self.width*0.1),int(self.height*0.05))
        importBtn = QPushButton("Import CSV", parent = self.window)
        importBtn.setGeometry(int(self.width*2/3-self.width*0.1),int(self.height*0.05),int(self.width*0.1),int(self.height*0.05))
        importBtn.clicked.connect(self.importCsv)
        exportBtn = QPushButton("Export CSV", parent = self.window)
        exportBtn.setGeometry(int(self.width*2/3),int(self.height *0.05),int(self.width*0.1),int(self.height*0.05))
        exportBtn.clicked.connect(self.exportCsv)

    def importCsv(self):
        self.filename, _ = QFileDialog.getOpenFileName(parent=self.window)

        self.transactions = []
        with open(self.filename, "r") as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                self.transactions.append(transaction(row))

    def exportCsv(self):
        print()

    def categorize(self):
        print()
