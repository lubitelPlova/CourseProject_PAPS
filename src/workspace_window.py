from PyQt5 import QtWidgets
from workspace import Ui_WorkspaceWindow
from notification_window import NotificationWindow
from PandasModel import PandasModel
import pandas as pd
from Data import Proxy, RealData
from PyQt5.QtWidgets import QMessageBox, QAbstractItemView
from AnalyzeStrategy import *
from PlotReady import PlotReadyWindow

class WorkspaceWindow(QtWidgets.QMainWindow, Ui_WorkspaceWindow): #
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_7.clicked.connect(self.openNotificationWindow)
        self.pushButton_4.clicked.connect(self.openData)
        self.pushButton.clicked.connect(self.addData)
        self.pushButton_2.clicked.connect(self.deleteData)
        self.pushButton_3.clicked.connect(self.changeData)
        self.pushButton_8.clicked.connect(self.openPlotReady)
        self.notificationWindow = None
        self.plotReadyWindow = None
        self.dataProxy = Proxy(RealData(), 1)
        self.analyzer = Analyzer()
        
        # self.tableView.currentChanged.connect(self.analyzeData)

    def openNotificationWindow(self):
        self.notificationWindow = NotificationWindow()
        self.notificationWindow.show()

    def openData(self):
        self.dataProxy.open("data.csv")
        df = self.dataProxy.getData()
        model = PandasModel(df)
        self.tableView.setModel(model)
        self.tableView.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectColumns)
        self.tableView.selectionModel().selectionChanged.connect(self.analyzeData)
        
    def deleteData(self):
        if (self.dataProxy.add_line()):
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Удаление выполнено!")
            msgBox.exec_()
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Удаление не выполнено!")
            msgBox.exec_()

    def changeData(self):
        if (self.dataProxy.add_line()):
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Изменение выполнено!")
            msgBox.exec_()
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Изменение не выполнено!")
            msgBox.exec_()

    def addData(self):
        if (self.dataProxy.add_line()):
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Добавление выполнено!")
            msgBox.exec_()
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Добавление не выполнено!")
            msgBox.exec_()  

    def openPlotReady(self):
        self.plotReadyWindow = PlotReadyWindow()
        self.plotReadyWindow.show()

    def analyzeData(self, selected, not_selected):

        if selected.indexes():
            index = selected.indexes()[0].column()
            print(f"Выбран столбец: {selected.indexes()[0].column()}")
            df = self.dataProxy.getData()
            text = self.analyzer.analyze_data(df, index)
            self.textBrowser.clear()
            self.textBrowser.append(f"Выбран столбец: {index}\n")
            self.textBrowser.append(text)
