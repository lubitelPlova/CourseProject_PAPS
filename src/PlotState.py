from abc import ABC, abstractmethod

class VisualizationState(ABC): # абстрактный интерфейс State
    @abstractmethod
    def visualize(self, widget):
        pass

class LineChartState(VisualizationState): # конкретная реализация State
    def visualize(self, widget):
        widget.axis.clear()
        widget.axis.plot(widget.x, widget.y)
        widget.canvas.draw()
        print("Визуализация данных в виде линейного графика")

class HistogramState(VisualizationState): # конкретная реализация State
    def visualize(self, widget):
        widget.axis.clear()
        widget.axis.hist(widget.y, bins=10)
        widget.canvas.draw()
        print("Визуализация данных в виде гистограммы")

class HeatmapState(VisualizationState): # конкретная реализация State
    def visualize(self, widget):
        widget.axis.clear()
        heatmap_data = widget.x.reshape((len(widget.x), 1))
        widget.axis.imshow(heatmap_data, cmap='hot', interpolation='nearest')
        widget.canvas.draw()
        print("Визуализация данных в виде тепловой карты")