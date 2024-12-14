from abc import ABC, abstractmethod
import numpy as np
import pandas as pd

# Абстрактный класс Стратегия
class AnalysisStrategy(ABC):
    @abstractmethod
    def analyze(self, data):
        pass
# Стратегия для числовых данных
class NumericalAnalysisStrategy(AnalysisStrategy):
    def analyze(self, data):
        result = "Численная переменная:\n"
        result += f"Среднее: {np.mean(data)}\n"
        result += f"Минимум: {np.min(data)}\n"
        result += f"Максимум: {np.max(data)}\n"
        result += f"Квантили: {np.quantile(data, [0.25, 0.5, 0.75])}\n"
        result += f"Стандартное отклонение: {np.std(data)}\n"
        return result
# Стратегия для категориальных данных
class CategoricalAnalysisStrategy(AnalysisStrategy):
    def analyze(self, data):
        result = "Категориальная переменная:\n"
        result += f"Уникальные значения: {np.unique(data)}\n"
        result += f"Частота каждого значения: {np.unique(data, return_counts=True)}\n"
        return result
# Стратегия для текстовых данных
class TextAnalysisStrategy(AnalysisStrategy):
    def analyze(self, data):
        result = "Текстовая переменная:\n"
        result += f"Количество слов: {len(data)}\n"
        result += f"Уникальные слова: {np.unique(data)}\n"
        return result
    
class Analyzer:

    def __init__(self):
        self.strategy = None


    def set_strategy(self, strategy):
        self.strategy = strategy

    def analyze_data(self, data: pd.DataFrame, index):
        result = ""
        
        if data.iloc[:,index].nunique() < 10:
            print("Categorical")
            self.set_strategy(CategoricalAnalysisStrategy())
        else:
            if data.iloc[:, index].dtype == "object":
                print('String object type')
                self.set_strategy(TextAnalysisStrategy())
            else:
                print('Numeric')
                self.set_strategy(NumericalAnalysisStrategy())

        if self.strategy:
            result += self.strategy.analyze(data.iloc[:, index])

        return result