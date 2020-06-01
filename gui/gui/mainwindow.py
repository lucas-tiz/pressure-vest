# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(60, 40, 91, 17))
        self.label.setObjectName("label")
        self.horizontalSlider_chamber1 = QtWidgets.QSlider(self.centralWidget)
        self.horizontalSlider_chamber1.setGeometry(QtCore.QRect(30, 90, 160, 29))
        self.horizontalSlider_chamber1.setMaximum(100)
        self.horizontalSlider_chamber1.setSingleStep(0)
        self.horizontalSlider_chamber1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_chamber1.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_chamber1.setObjectName("horizontalSlider_chamber1")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(70, 120, 91, 17))
        self.label_2.setObjectName("label_2")
        self.doubleSpinBox_chamber1 = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.doubleSpinBox_chamber1.setGeometry(QtCore.QRect(80, 70, 69, 27))
        self.doubleSpinBox_chamber1.setMaximum(5.0)
        self.doubleSpinBox_chamber1.setSingleStep(0.1)
        self.doubleSpinBox_chamber1.setObjectName("doubleSpinBox_chamber1")
        self.pushButton_start = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_start.setGeometry(QtCore.QRect(60, 190, 99, 27))
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_stop = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_stop.setGeometry(QtCore.QRect(180, 190, 99, 27))
        self.pushButton_stop.setObjectName("pushButton_stop")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 25))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Chamber 1"))
        self.label_2.setText(_translate("MainWindow", "pressure (psi)"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))
        self.pushButton_stop.setText(_translate("MainWindow", "Stop"))

