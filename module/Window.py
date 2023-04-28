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
        #button for categorizatino
        catBtn = QPushButton("categorize",parent=self.window)
        catBtn.setGeometry(int(self.width/3-self.width*0.1),int(self.height*0.05),int(self.width*0.1),int(self.height*0.05))
        catBtn.clicked.connect(self.categorize)
        #input field for categorie
        inputCat = QPlainTextEdit(parent=self.window)
        inputCat.setGeometry(int(self.width/3),int(self.height*0.05),int(self.width*0.1),int(self.height*0.05))
        #button for csv input
        importBtn = QPushButton("Import CSV", parent = self.window)
        importBtn.setGeometry(int(self.width*2/3-self.width*0.1),int(self.height*0.05),int(self.width*0.1),int(self.height*0.05))
        importBtn.clicked.connect(self.importCsv)
        #button for csv export
        exportBtn = QPushButton("Export CSV", parent = self.window)
        exportBtn.setGeometry(int(self.width*2/3),int(self.height *0.05),int(self.width*0.1),int(self.height*0.05))
        exportBtn.clicked.connect(self.exportCsv)
        #initiate Table
        self.table = QTableWidget(parent=self.window)
        self.table.setGeometry(int(self.width/8),int(self.height*1/5),int(self.width*3/4),int(self.height*3/5))
        self.table.setColumnCount(6)
        #set widths of the column
        self.table.setColumnWidth(0,int(self.width/10))
        self.table.setColumnWidth(1,int(self.width/10))
        self.table.setColumnWidth(2,int(self.width/10))
        self.table.setColumnWidth(3,int(self.width/10))
        self.table.setColumnWidth(4,int(self.width/4))
        self.table.setColumnWidth(5,int(self.width/10))

    #import the transactions from as csv and add them to the table
    def importCsv(self):
        self.filename, _ = QFileDialog.getOpenFileName(parent=self.window)
        self.transactions = []
        with open(self.filename, "r") as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                self.transactions.append(transaction(row))
        self.fillTable()
    #add to the table
    def fillTable(self):
        transactionCounter = 0
        self.table.setRowCount(len(self.transactions))
        for tr in self.transactions:
            for i in range(0,6):
                self.table.setItem(transactionCounter,i,QTableWidgetItem(tr.data[i]))
            transactionCounter +=1
    def exportCsv(self):
        print()

    def categorize(self):
        print()
