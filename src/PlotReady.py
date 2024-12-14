from PyQt5 import QtWidgets
from visualdata import Ui_MainWindow
from Data import Proxy, RealData
from PandasModel import PandasModel
from PlotWidget import MatplotlibWidget
from PlotState import *
from PyQt5.QtWidgets import QMessageBox, QTableView

class PlotReadyWindow(QtWidgets.QMainWindow, Ui_MainWindow): #
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dataProxy = Proxy(RealData(), 1)
        self.dataProxy.open("data.csv")
        self.data = self.dataProxy.getData()
        model = PandasModel(self.data)
        self.tableView.setModel(model)
        self.tableView.setSelectionBehavior(QTableView.SelectItems)
        self.tableView.setSelectionMode(QTableView.ExtendedSelection)
        self.pushButton.clicked.connect(self.VisualisePlot)
        self.plotter = None
        self.state = LineChartState()

    def VisualisePlot(self):

        selected_columns = self.tableView.selectionModel().selectedColumns()

        if len(selected_columns) != 2:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Выберите 2 столбца")
            msgBox.exec_()
            return 

        x_column = selected_columns[0].column()
        y_column = selected_columns[1].column()
        x = self.data.iloc[:, x_column].values
        y = self.data.iloc[:, y_column].values


        self.plotter = MatplotlibWidget(x, y)
        if (self.radioButton.isChecked()):
            pass
        elif (self.radioButton_2.isChecked()):
            self.state = HistogramState()
        elif (self.radioButton_3.isChecked()):
            self.state = HeatmapState
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Не выбран тип графика")
            msgBox.exec_()
            return 
        self.plotter.set_state(self.state)
        self.plotter.plot()
        self.plotter.show()