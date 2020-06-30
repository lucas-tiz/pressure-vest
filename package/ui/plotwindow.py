# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/plotwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(749, 314)
        self.widget_chamberPlot = PlotWidget(Form)
        self.widget_chamberPlot.setGeometry(QtCore.QRect(40, 40, 661, 231))
        self.widget_chamberPlot.setObjectName("widget_chamberPlot")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

from pyqtgraph import PlotWidget
