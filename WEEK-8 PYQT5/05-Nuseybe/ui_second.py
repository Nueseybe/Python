# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\karakurt\Documents\GitHub\homework\WEEK-8 PYQT5\05-Nuseybe\second.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 315)
        MainWindow.setMinimumSize(QtCore.QSize(400, 250))
        MainWindow.setMaximumSize(QtCore.QSize(500, 500))
        MainWindow.setStyleSheet("background-color: rgb(251, 231, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 371, 41))
        self.label.setStyleSheet("font: 63 14pt \"Montserrat SemiBold\";\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 71, 61))
        self.label_2.setStyleSheet("font: 63 14pt \"Montserrat SemiBold\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.limit = QtWidgets.QSlider(self.centralwidget)
        self.limit.setGeometry(QtCore.QRect(100, 140, 361, 41))
        self.limit.setMaximum(30)
        self.limit.setPageStep(2)
        self.limit.setOrientation(QtCore.Qt.Horizontal)
        self.limit.setObjectName("limit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 100, 61, 31))
        self.label_3.setStyleSheet("font: 63 14pt \"Montserrat SemiBold\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(440, 100, 61, 31))
        self.label_4.setStyleSheet("font: 63 14pt \"Montserrat SemiBold\";")
        self.label_4.setObjectName("label_4")
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(360, 220, 93, 31))
        self.okButton.setStyleSheet("font: 63 11pt \"Montserrat SemiBold\";\n"
"background-color: rgb(85, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.okButton.setObjectName("okButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Please select the time"))
        self.label_2.setText(_translate("MainWindow", "Time"))
        self.label_3.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "30"))
        self.okButton.setText(_translate("MainWindow", "OK"))
