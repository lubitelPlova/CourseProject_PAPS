# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\data_workspace.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WorkspaceWindow(object):
    def setupUi(self, WorkspaceWindow):
        WorkspaceWindow.setObjectName("WorkspaceWindow")
        WorkspaceWindow.resize(851, 697)
        WorkspaceWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(WorkspaceWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(10)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(10)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_2.addWidget(self.pushButton_8)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 1, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 180))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 2, 0, 1, 2)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        WorkspaceWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(WorkspaceWindow)
        self.statusbar.setObjectName("statusbar")
        WorkspaceWindow.setStatusBar(self.statusbar)

        self.retranslateUi(WorkspaceWindow)
        QtCore.QMetaObject.connectSlotsByName(WorkspaceWindow)

    def retranslateUi(self, WorkspaceWindow):
        _translate = QtCore.QCoreApplication.translate
        WorkspaceWindow.setWindowTitle(_translate("WorkspaceWindow", "Система анализа медицинских данных \"Багульник\""))
        self.pushButton.setText(_translate("WorkspaceWindow", "Добавить"))
        self.pushButton_2.setText(_translate("WorkspaceWindow", "Удалить"))
        self.pushButton_3.setText(_translate("WorkspaceWindow", "Изменить"))
        self.pushButton_8.setText(_translate("WorkspaceWindow", "Визуализация"))
        self.pushButton_7.setText(_translate("WorkspaceWindow", "Уведомления"))
        self.pushButton_4.setText(_translate("WorkspaceWindow", "Открыть"))
        self.pushButton_5.setText(_translate("WorkspaceWindow", "Обновить"))
        self.pushButton_6.setText(_translate("WorkspaceWindow", "Сохранить"))
