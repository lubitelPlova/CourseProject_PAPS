# import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PlotState import *

class MatplotlibWidget(QWidget): # реализация Context
    def __init__(self, x, y, parent=None):
        super().__init__(parent)
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.axis = self.figure.add_subplot(111)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)
        self.x = x
        self.y = y
        self._state = LineChartState()  # Начальное состояние

    def set_state(self, state: VisualizationState):
        self._state = state

    def plot(self):
        self._state.visualize(self)