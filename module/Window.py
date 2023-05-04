import csv
import os.path

from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from screeninfo import get_monitors
import sys
from module.CSVReader import *
from module.transaction import transaction


class MWindow:
    def __init__(self, name):
        self.transactions = readInit()
        self.filename = None
        self.lastClicked = None
        self.app = QApplication([])
        self.window = QWidget()
        self.window.setWindowTitle(name)
        self.getScreenSize()
        self.window.setGeometry(0, 0, int(self.width * 0.99), int(self.height * 0.99))
        self.addElements()
        self.fillTable()
        self.window.show()
        self.app.aboutToQuit.connect(lambda :writeExit(self.transactions))
        sys.exit(self.app.exec())

    def getScreenSize(self):
        self.width = 0
        self.height = 0
        for monitor in get_monitors():
            if monitor.width > self.width:
                self.width = monitor.width
                self.height = monitor.height

    def addElements(self):
        # button for categorizatino
        resBtn = QPushButton("reset CSV",parent=self.window)
        resBtn.setGeometry(0,self.height*0.05,int(self.width*0.1),int(self.height*0.05))
        resBtn.clicked.connect(self.resetFile)
        catBtn = QPushButton("categorize", parent=self.window)
        catBtn.setGeometry(int(self.width / 3 - self.width * 0.1), int(self.height * 0.05), int(self.width * 0.1),
                           int(self.height * 0.05))
        catBtn.clicked.connect(self.categorize)
        # input field for categorie
        self.inputCat = QLineEdit(parent=self.window)
        self.inputCat.editingFinished.connect(self.categorize)
        self.inputCat.setGeometry(int(self.width / 3), int(self.height * 0.05), int(self.width * 0.1),
                                  int(self.height * 0.05))
        # button for csv input
        importBtn = QPushButton("Import CSV", parent=self.window)
        importBtn.setGeometry(int(self.width * 2 / 3 - self.width * 0.1), int(self.height * 0.05),
                              int(self.width * 0.1), int(self.height * 0.05))
        importBtn.clicked.connect(self.importCsv)
        # button for csv export
        exportBtn = QPushButton("Export CSV", parent=self.window)
        exportBtn.setGeometry(int(self.width * 2 / 3), int(self.height * 0.05), int(self.width * 0.1),
                              int(self.height * 0.05))
        exportBtn.clicked.connect(self.exportCsv)
        # initiate Table
        self.table = QTableWidget(parent=self.window)
        self.table.setGeometry(int(self.width / 8), int(self.height * 1 / 5), int(self.width * 3 / 4),
                               int(self.height * 3 / 5))
        self.table.setColumnCount(6)
        self.table.doubleClicked.connect(self.setLastClicked)
        self.table.itemChanged.connect(self.changedItem)
        self.table.sortItems(3, QtCore.Qt.SortOrder.AscendingOrder)
        # set widths of the column
        self.table.setColumnWidth(0, int(self.width / 10))
        self.table.setColumnWidth(1, int(self.width / 10))
        self.table.setColumnWidth(2, int(self.width / 10))
        self.table.setColumnWidth(3, int(self.width / 10))
        self.table.setColumnWidth(4, int(self.width / 4))
        self.table.setColumnWidth(5, int(self.width / 10))
    def setLastClicked(self,item):
        self.lastClicked = item
    def changedItem(self,item):
        row = int(item.row())
        if self.lastClicked is not None and self.lastClicked.row() == row and self.lastClicked.column() == item.column():
            self.lastClicked = None
            self.recieverToCategorie(self.transactions[row].reciever,item.text())
    def resetFile(self):
        resetDefault()
        self.transactions = readInit()
        self.fillTable()


    # import the transactions from as csv and add them to the table
    def importCsv(self):

        self.filename, _ = QFileDialog.getOpenFileName(parent=self.window)
        if not self.filename =="":
            reader = CSVReader(self.filename,self.transactions)
            self.transactions = reader.transactions
        self.fillTable()

    # add to the table
    def fillTable(self):
        transactionCounter = 0
        self.table.setRowCount(len(self.transactions))
        for tr in self.transactions:
            for i in range(0, 6):
                self.table.setItem(transactionCounter, i, QTableWidgetItem(tr.data[i]))
            transactionCounter += 1

    #export the transaction list to a by the user specified location as a csv file
    def exportCsv(self):
        directory = QFileDialog.getExistingDirectory()
        if(os.path.isfile(directory+"/umsatzCategorized.csv")):
            name = ""
            for i in range(2,20):
                name = "/umsatzCategorized("+str(i)+").csv"
                if not os.path.isfile(directory+name):
                    break
        with open(directory+name,"w") as file:
            for tr in self.transactions:
                file.write(tr.asString())
            file.close()

    # take the input value , write it into to categorie column in the table and change the propertie of the transaction
    def categorize(self):
        selectedIndexes = self.table.selectedIndexes()
        inputValue = self.inputCat.text()
        for index in selectedIndexes:
            row = index.row()
            self.transactions[row].categorie = inputValue
            self.table.setItem(row, 1, QTableWidgetItem(inputValue))
            self.recieverToCategorie(self.transactions[row].reciever, inputValue)

    # if categorie gets change for an specific reciever the method search every transaction with this reciever and
    # change the categorie of this transactions
    def recieverToCategorie(self, reciever, categorie):
        trCounter = 0
        for tr in self.transactions:
            if tr.reciever == reciever and reciever != "Unknown":
                tr.categorie = categorie
                tr.data[1] = categorie
                self.table.setItem(trCounter, 1, QTableWidgetItem(categorie))
            trCounter += 1
