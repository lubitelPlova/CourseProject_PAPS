from abc import ABC, abstractmethod
import pandas as pd
import requests as r
import io

class Data(): # Интерфейс для работы с данными
    _data = None
    @abstractmethod
    def __init__():
        pass

    @abstractmethod
    def open(self, dataname: str):
        pass

    @abstractmethod
    def getData(self) -> pd.DataFrame:
        return self._data

    @abstractmethod
    def reload(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def change_line(self):
        pass

    @abstractmethod
    def delete_line(self):
        pass

    @abstractmethod
    def add_line(self):
        pass

class RealData(Data): #Класс данных, реализующий интерфейс
    def __init__(self):
        self._data = None

    def getData(self):
        return self._data
    
    def open(self, dataname):
        response = r.get("http://localhost:5000/data", params = {"filename": dataname})
        # self._data = pd.read_csv(response.content)
        # print(type(self._data))
        if response.status_code == 200:
        # Записываем содержимое файла в файловую переменную
            with open('data.csv', 'wb') as f:
                f.write(response.content)

                # Читаем файл с помощью pd.read_csv()
                self._data = pd.read_csv('data.csv')
                print(type(self._data))
            
        else:
            print('Ошибка скачивания файла')



    def reload(self):
        print("Данные обновлены!")

    def save(self):
        print("Данные сохранены!")

    def change_line(self):
        print("Данные изменены!")

    def delete_line(self):
        print("Данные удалены!")

    def add_line(self):
        print("Данные добавлены!")


class Proxy(Data): #Класс Прокси, контролирующий доступ к файлам
    def __init__(self, real_data: RealData, user_access_level: int):
        self._real_data = real_data
        self._user_access_level = user_access_level

    def open(self, dataname: str):
        self._real_data.open(dataname)

    def getData(self) -> pd.DataFrame:
        return self._real_data.getData()

    def reload(self):
        self._real_data.reload()

    def save(self):
        self._real_data.save()

    def change_line(self):
        if self._user_access_level == 2:
            self._real_data.change_line()
            return True
        else:
            print("У вас нет доступа к этому методу")
            return False

    def delete_line(self):
        if self._user_access_level == 2:
            self._real_data.delete_line()
            return True
        else:
            print("У вас нет доступа к этому методу")
            return False

    def add_line(self):
        if self._user_access_level == 2:
            self._real_data.add_line()
            return True
        else:
            print("У вас нет доступа к этому методу")
            return False