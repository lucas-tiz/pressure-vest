# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(505, 638)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(212, 20, 78, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_on = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_on.setGeometry(QtCore.QRect(280, 517, 85, 27))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_on.setFont(font)
        self.pushButton_on.setStyleSheet("background-color: rgb(0, 190, 0);\n"
"background-color: rgb(0, 170, 0);")
        self.pushButton_on.setObjectName("pushButton_on")
        self.label_9 = QtWidgets.QLabel(self.centralWidget)
        self.label_9.setGeometry(QtCore.QRect(20, 522, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.groupBox_alr = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_alr.setGeometry(QtCore.QRect(76, 250, 162, 146))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_alr.sizePolicy().hasHeightForWidth())
        self.groupBox_alr.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_alr.setFont(font)
        self.groupBox_alr.setStyleSheet("QGroupBox { border:none}")
        self.groupBox_alr.setCheckable(True)
        self.groupBox_alr.setObjectName("groupBox_alr")
        self.frame_alr = QtWidgets.QFrame(self.groupBox_alr)
        self.frame_alr.setGeometry(QtCore.QRect(4, 24, 154, 120))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_alr.sizePolicy().hasHeightForWidth())
        self.frame_alr.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.frame_alr.setFont(font)
        self.frame_alr.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_alr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_alr.setLineWidth(1)
        self.frame_alr.setObjectName("frame_alr")
        self.horizontalSlider_alr = QtWidgets.QSlider(self.frame_alr)
        self.horizontalSlider_alr.setGeometry(QtCore.QRect(9, 41, 131, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_alr.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_alr.setSizePolicy(sizePolicy)
        self.horizontalSlider_alr.setStyleSheet("selection-background-color: rgb(141, 70, 212);")
        self.horizontalSlider_alr.setMaximum(100)
        self.horizontalSlider_alr.setSingleStep(0)
        self.horizontalSlider_alr.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_alr.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider_alr.setObjectName("horizontalSlider_alr")
        self.line_4 = QtWidgets.QFrame(self.frame_alr)
        self.line_4.setGeometry(QtCore.QRect(9, 68, 136, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_16 = QtWidgets.QLabel(self.frame_alr)
        self.label_16.setGeometry(QtCore.QRect(66, 12, 78, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.doubleSpinBox_alr = QtWidgets.QDoubleSpinBox(self.frame_alr)
        self.doubleSpinBox_alr.setGeometry(QtCore.QRect(10, 8, 50, 27))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_alr.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_alr.setSizePolicy(sizePolicy)
        self.doubleSpinBox_alr.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.doubleSpinBox_alr.setFont(font)
        self.doubleSpinBox_alr.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_alr.setDecimals(1)
        self.doubleSpinBox_alr.setMaximum(5.0)
        self.doubleSpinBox_alr.setSingleStep(0.1)
        self.doubleSpinBox_alr.setObjectName("doubleSpinBox_alr")
        self.label_17 = QtWidgets.QLabel(self.frame_alr)
        self.label_17.setGeometry(QtCore.QRect(72, 90, 72, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.label_alr = QtWidgets.QLabel(self.frame_alr)
        self.label_alr.setEnabled(True)
        self.label_alr.setGeometry(QtCore.QRect(10, 86, 35, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_alr.sizePolicy().hasHeightForWidth())
        self.label_alr.setSizePolicy(sizePolicy)
        self.label_alr.setMinimumSize(QtCore.QSize(0, 25))
        self.label_alr.setAutoFillBackground(False)
        self.label_alr.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(196, 193, 189);")
        self.label_alr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_alr.setAlignment(QtCore.Qt.AlignCenter)
        self.label_alr.setObjectName("label_alr")
        self.label_alr_color = QtWidgets.QLabel(self.groupBox_alr)
        self.label_alr_color.setGeometry(QtCore.QRect(0, 23, 161, 121))
        self.label_alr_color.setStyleSheet("background-color: rgba(236, 177, 32, 100);\n"
"background-color: rgb(170, 170, 255, 150);\n"
"border-radius: 10px;")
        self.label_alr_color.setText("")
        self.label_alr_color.setObjectName("label_alr_color")
        self.label_alr_color.raise_()
        self.frame_alr.raise_()
        self.groupBox_aur = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_aur.setGeometry(QtCore.QRect(76, 79, 162, 146))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_aur.sizePolicy().hasHeightForWidth())
        self.groupBox_aur.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_aur.setFont(font)
        self.groupBox_aur.setStyleSheet("QGroupBox { border:none}")
        self.groupBox_aur.setFlat(True)
        self.groupBox_aur.setCheckable(True)
        self.groupBox_aur.setObjectName("groupBox_aur")
        self.frame_aur = QtWidgets.QFrame(self.groupBox_aur)
        self.frame_aur.setEnabled(True)
        self.frame_aur.setGeometry(QtCore.QRect(4, 24, 156, 120))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_aur.sizePolicy().hasHeightForWidth())
        self.frame_aur.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.frame_aur.setFont(font)
        self.frame_aur.setStyleSheet("")
        self.frame_aur.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_aur.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_aur.setLineWidth(1)
        self.frame_aur.setObjectName("frame_aur")
        self.horizontalSlider_aur = QtWidgets.QSlider(self.frame_aur)
        self.horizontalSlider_aur.setGeometry(QtCore.QRect(9, 41, 131, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_aur.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_aur.setSizePolicy(sizePolicy)
        self.horizontalSlider_aur.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"selection-background-color: rgb(0, 114, 189);\n"
"")
        self.horizontalSlider_aur.setMaximum(100)
        self.horizontalSlider_aur.setSingleStep(0)
        self.horizontalSlider_aur.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_aur.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider_aur.setObjectName("horizontalSlider_aur")
        self.line_5 = QtWidgets.QFrame(self.frame_aur)
        self.line_5.setGeometry(QtCore.QRect(9, 68, 136, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_5.sizePolicy().hasHeightForWidth())
        self.line_5.setSizePolicy(sizePolicy)
        self.line_5.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_19 = QtWidgets.QLabel(self.frame_aur)
        self.label_19.setGeometry(QtCore.QRect(66, 12, 78, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.doubleSpinBox_aur = QtWidgets.QDoubleSpinBox(self.frame_aur)
        self.doubleSpinBox_aur.setGeometry(QtCore.QRect(10, 8, 50, 27))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_aur.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_aur.setSizePolicy(sizePolicy)
        self.doubleSpinBox_aur.setMaximumSize(QtCore.QSize(50, 16777215))
        self.doubleSpinBox_aur.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.doubleSpinBox_aur.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_aur.setDecimals(1)
        self.doubleSpinBox_aur.setMaximum(5.0)
        self.doubleSpinBox_aur.setSingleStep(0.1)
        self.doubleSpinBox_aur.setObjectName("doubleSpinBox_aur")
        self.label_20 = QtWidgets.QLabel(self.frame_aur)
        self.label_20.setGeometry(QtCore.QRect(72, 90, 72, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.label_aur = QtWidgets.QLabel(self.frame_aur)
        self.label_aur.setEnabled(True)
        self.label_aur.setGeometry(QtCore.QRect(10, 86, 35, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_aur.sizePolicy().hasHeightForWidth())
        self.label_aur.setSizePolicy(sizePolicy)
        self.label_aur.setMinimumSize(QtCore.QSize(0, 25))
        self.label_aur.setAutoFillBackground(False)
        self.label_aur.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(196, 193, 189);")
        self.label_aur.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_aur.setAlignment(QtCore.Qt.AlignCenter)
        self.label_aur.setObjectName("label_aur")
        self.label_aur_color = QtWidgets.QLabel(self.groupBox_aur)
        self.label_aur_color.setGeometry(QtCore.QRect(0, 23, 161, 121))
        self.label_aur_color.setStyleSheet("background-color: rgba(0, 170, 255, 100);\n"
"background-color: rgb(52, 141, 200, 150);\n"
"background-color: rgb(53, 151, 255, 130);\n"
"border-radius: 10px;")
        self.label_aur_color.setText("")
        self.label_aur_color.setObjectName("label_aur_color")
        self.label_aur_color.raise_()
        self.frame_aur.raise_()
        self.groupBox_all = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_all.setGeometry(QtCore.QRect(266, 249, 162, 146))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_all.sizePolicy().hasHeightForWidth())
        self.groupBox_all.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_all.setFont(font)
        self.groupBox_all.setStyleSheet("QGroupBox { border:none}")
        self.groupBox_all.setCheckable(True)
        self.groupBox_all.setObjectName("groupBox_all")
        self.frame_all = QtWidgets.QFrame(self.groupBox_all)
        self.frame_all.setGeometry(QtCore.QRect(4, 24, 154, 120))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_all.sizePolicy().hasHeightForWidth())
        self.frame_all.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.frame_all.setFont(font)
        self.frame_all.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_all.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_all.setLineWidth(1)
        self.frame_all.setObjectName("frame_all")
        self.horizontalSlider_all = QtWidgets.QSlider(self.frame_all)
        self.horizontalSlider_all.setGeometry(QtCore.QRect(9, 41, 131, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_all.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_all.setSizePolicy(sizePolicy)
        self.horizontalSlider_all.setStyleSheet("selection-background-color: rgb(119, 172, 48);\n"
"selection-background-color: rgb(0, 170, 0);")
        self.horizontalSlider_all.setMaximum(100)
        self.horizontalSlider_all.setSingleStep(0)
        self.horizontalSlider_all.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_all.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider_all.setObjectName("horizontalSlider_all")
        self.line_6 = QtWidgets.QFrame(self.frame_all)
        self.line_6.setGeometry(QtCore.QRect(9, 68, 136, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_6.sizePolicy().hasHeightForWidth())
        self.line_6.setSizePolicy(sizePolicy)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label_22 = QtWidgets.QLabel(self.frame_all)
        self.label_22.setGeometry(QtCore.QRect(66, 12, 78, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.doubleSpinBox_all = QtWidgets.QDoubleSpinBox(self.frame_all)
        self.doubleSpinBox_all.setGeometry(QtCore.QRect(10, 8, 50, 27))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_all.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_all.setSizePolicy(sizePolicy)
        self.doubleSpinBox_all.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.doubleSpinBox_all.setFont(font)
        self.doubleSpinBox_all.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_all.setDecimals(1)
        self.doubleSpinBox_all.setMaximum(5.0)
        self.doubleSpinBox_all.setSingleStep(0.1)
        self.doubleSpinBox_all.setObjectName("doubleSpinBox_all")
        self.label_23 = QtWidgets.QLabel(self.frame_all)
        self.label_23.setGeometry(QtCore.QRect(72, 90, 72, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.label_all = QtWidgets.QLabel(self.frame_all)
        self.label_all.setEnabled(True)
        self.label_all.setGeometry(QtCore.QRect(10, 86, 35, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_all.sizePolicy().hasHeightForWidth())
        self.label_all.setSizePolicy(sizePolicy)
        self.label_all.setMinimumSize(QtCore.QSize(0, 25))
        self.label_all.setAutoFillBackground(False)
        self.label_all.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(196, 193, 189);")
        self.label_all.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_all.setAlignment(QtCore.Qt.AlignCenter)
        self.label_all.setObjectName("label_all")
        self.label_all_color = QtWidgets.QLabel(self.groupBox_all)
        self.label_all_color.setGeometry(QtCore.QRect(0, 23, 161, 121))
        self.label_all_color.setStyleSheet("background-color: rgba(119, 172, 48, 100);\n"
"background-color: rgb(173, 206, 130, 150);\n"
"border-radius: 10px;")
        self.label_all_color.setText("")
        self.label_all_color.setObjectName("label_all_color")
        self.label_all_color.raise_()
        self.frame_all.raise_()
        self.groupBox_aul = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_aul.setGeometry(QtCore.QRect(266, 79, 162, 146))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_aul.sizePolicy().hasHeightForWidth())
        self.groupBox_aul.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_aul.setFont(font)
        self.groupBox_aul.setStyleSheet("QGroupBox { border:none}")
        self.groupBox_aul.setFlat(True)
        self.groupBox_aul.setCheckable(True)
        self.groupBox_aul.setObjectName("groupBox_aul")
        self.frame_aul = QtWidgets.QFrame(self.groupBox_aul)
        self.frame_aul.setGeometry(QtCore.QRect(4, 24, 154, 120))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_aul.sizePolicy().hasHeightForWidth())
        self.frame_aul.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.frame_aul.setFont(font)
        self.frame_aul.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_aul.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_aul.setLineWidth(1)
        self.frame_aul.setObjectName("frame_aul")
        self.horizontalSlider_aul = QtWidgets.QSlider(self.frame_aul)
        self.horizontalSlider_aul.setGeometry(QtCore.QRect(9, 41, 131, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider_aul.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_aul.setSizePolicy(sizePolicy)
        self.horizontalSlider_aul.setStyleSheet("selection-background-color: rgb(216, 83, 25);")
        self.horizontalSlider_aul.setMaximum(100)
        self.horizontalSlider_aul.setSingleStep(0)
        self.horizontalSlider_aul.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_aul.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider_aul.setObjectName("horizontalSlider_aul")
        self.line_7 = QtWidgets.QFrame(self.frame_aul)
        self.line_7.setGeometry(QtCore.QRect(9, 68, 136, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_7.sizePolicy().hasHeightForWidth())
        self.line_7.setSizePolicy(sizePolicy)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.label_25 = QtWidgets.QLabel(self.frame_aul)
        self.label_25.setGeometry(QtCore.QRect(66, 12, 78, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.doubleSpinBox_aul = QtWidgets.QDoubleSpinBox(self.frame_aul)
        self.doubleSpinBox_aul.setGeometry(QtCore.QRect(10, 8, 50, 27))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_aul.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_aul.setSizePolicy(sizePolicy)
        self.doubleSpinBox_aul.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.doubleSpinBox_aul.setFont(font)
        self.doubleSpinBox_aul.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_aul.setDecimals(1)
        self.doubleSpinBox_aul.setMaximum(5.0)
        self.doubleSpinBox_aul.setSingleStep(0.1)
        self.doubleSpinBox_aul.setObjectName("doubleSpinBox_aul")
        self.label_26 = QtWidgets.QLabel(self.frame_aul)
        self.label_26.setGeometry(QtCore.QRect(72, 90, 72, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.label_aul = QtWidgets.QLabel(self.frame_aul)
        self.label_aul.setEnabled(True)
        self.label_aul.setGeometry(QtCore.QRect(10, 86, 35, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_aul.sizePolicy().hasHeightForWidth())
        self.label_aul.setSizePolicy(sizePolicy)
        self.label_aul.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_aul.setFont(font)
        self.label_aul.setAutoFillBackground(False)
        self.label_aul.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(196, 193, 189);")
        self.label_aul.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_aul.setAlignment(QtCore.Qt.AlignCenter)
        self.label_aul.setObjectName("label_aul")
        self.label_aul_color = QtWidgets.QLabel(self.groupBox_aul)
        self.label_aul_color.setGeometry(QtCore.QRect(0, 23, 161, 121))
        self.label_aul_color.setStyleSheet("background-color: rgba(216, 83, 25, 100);\n"
"background-color: rgb(231, 179, 156, 150);\n"
"background-color: rgba(221, 117, 72, 140);\n"
"border-radius: 10px;")
        self.label_aul_color.setText("")
        self.label_aul_color.setObjectName("label_aul_color")
        self.label_aul_color.raise_()
        self.frame_aul.raise_()
        self.label_t_run = QtWidgets.QLabel(self.centralWidget)
        self.label_t_run.setEnabled(True)
        self.label_t_run.setGeometry(QtCore.QRect(100, 517, 51, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_t_run.sizePolicy().hasHeightForWidth())
        self.label_t_run.setSizePolicy(sizePolicy)
        self.label_t_run.setMinimumSize(QtCore.QSize(0, 25))
        self.label_t_run.setAutoFillBackground(False)
        self.label_t_run.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(196, 193, 189);")
        self.label_t_run.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_t_run.setAlignment(QtCore.Qt.AlignCenter)
        self.label_t_run.setObjectName("label_t_run")
        self.label_21 = QtWidgets.QLabel(self.centralWidget)
        self.label_21.setGeometry(QtCore.QRect(160, 520, 41, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(14, 50, 471, 451))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("img/anterior.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_alr_color_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_alr_color_2.setGeometry(QtCore.QRect(560, 30, 161, 131))
        self.label_alr_color_2.setStyleSheet("background-color: rgba(0, 114, 189);")
        self.label_alr_color_2.setText("")
        self.label_alr_color_2.setObjectName("label_alr_color_2")
        self.label_alr_color_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_alr_color_3.setGeometry(QtCore.QRect(560, 450, 161, 131))
        self.label_alr_color_3.setStyleSheet("background-color: rgba(119, 172, 48);")
        self.label_alr_color_3.setText("")
        self.label_alr_color_3.setObjectName("label_alr_color_3")
        self.label_alr_color_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_alr_color_5.setGeometry(QtCore.QRect(560, 170, 161, 131))
        self.label_alr_color_5.setStyleSheet("background-color: rgba(216, 83, 25);")
        self.label_alr_color_5.setText("")
        self.label_alr_color_5.setObjectName("label_alr_color_5")
        self.label_alr_color_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_alr_color_6.setGeometry(QtCore.QRect(560, 310, 161, 131))
        self.label_alr_color_6.setStyleSheet("background-color: rgba(236, 177, 32);")
        self.label_alr_color_6.setText("")
        self.label_alr_color_6.setObjectName("label_alr_color_6")
        self.label_alr_color_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_alr_color_7.setGeometry(QtCore.QRect(730, 310, 161, 131))
        self.label_alr_color_7.setStyleSheet("background-color: rgba(236, 177, 32, 200);")
        self.label_alr_color_7.setText("")
        self.label_alr_color_7.setObjectName("label_alr_color_7")
        self.label_alr_color_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_alr_color_8.setGeometry(QtCore.QRect(730, 450, 161, 131))
        self.label_alr_color_8.setStyleSheet("background-color: rgba(119, 172, 48, 200);")
        self.label_alr_color_8.setText("")
        self.label_alr_color_8.setObjectName("label_alr_color_8")
        self.label_alr_color_9 = QtWidgets.QLabel(self.centralWidget)
        self.label_alr_color_9.setGeometry(QtCore.QRect(730, 170, 161, 131))
        self.label_alr_color_9.setStyleSheet("background-color: rgba(216, 83, 25, 200);")
        self.label_alr_color_9.setText("")
        self.label_alr_color_9.setObjectName("label_alr_color_9")
        self.label_alr_color_10 = QtWidgets.QLabel(self.centralWidget)
        self.label_alr_color_10.setGeometry(QtCore.QRect(730, 30, 161, 131))
        self.label_alr_color_10.setStyleSheet("background-color: rgba(0, 114, 189, 200);")
        self.label_alr_color_10.setText("")
        self.label_alr_color_10.setObjectName("label_alr_color_10")
        self.label_alr_color_11 = QtWidgets.QLabel(self.centralWidget)
        self.label_alr_color_11.setGeometry(QtCore.QRect(730, 590, 161, 131))
        self.label_alr_color_11.setStyleSheet("background-color: rgba(236, 177, 32, 100);\n"
"background-color: rgb(170, 170, 255, 150);")
        self.label_alr_color_11.setText("")
        self.label_alr_color_11.setObjectName("label_alr_color_11")
        self.label_alr_color_12 = QtWidgets.QLabel(self.centralWidget)
        self.label_alr_color_12.setGeometry(QtCore.QRect(560, 590, 161, 131))
        self.label_alr_color_12.setStyleSheet("background-color: rgb(144, 144, 216);\n"
"")
        self.label_alr_color_12.setText("")
        self.label_alr_color_12.setObjectName("label_alr_color_12")
        self.label_2.raise_()
        self.label.raise_()
        self.pushButton_on.raise_()
        self.label_9.raise_()
        self.groupBox_alr.raise_()
        self.groupBox_aur.raise_()
        self.groupBox_all.raise_()
        self.groupBox_aul.raise_()
        self.label_t_run.raise_()
        self.label_21.raise_()
        self.label_alr_color_2.raise_()
        self.label_alr_color_3.raise_()
        self.label_alr_color_5.raise_()
        self.label_alr_color_6.raise_()
        self.label_alr_color_7.raise_()
        self.label_alr_color_8.raise_()
        self.label_alr_color_9.raise_()
        self.label_alr_color_10.raise_()
        self.label_alr_color_11.raise_()
        self.label_alr_color_12.raise_()
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 505, 25))
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
        self.label.setText(_translate("MainWindow", "Anterior"))
        self.pushButton_on.setText(_translate("MainWindow", "Run"))
        self.label_9.setText(_translate("MainWindow", "Run Time"))
        self.groupBox_alr.setTitle(_translate("MainWindow", "Lower Right"))
        self.label_16.setText(_translate("MainWindow", "setpoint (psi)"))
        self.label_17.setText(_translate("MainWindow", "current (psi)"))
        self.label_alr.setText(_translate("MainWindow", "0.0"))
        self.groupBox_aur.setTitle(_translate("MainWindow", "Upper Right"))
        self.label_19.setText(_translate("MainWindow", "setpoint (psi)"))
        self.label_20.setText(_translate("MainWindow", "current (psi)"))
        self.label_aur.setText(_translate("MainWindow", "0.0"))
        self.groupBox_all.setTitle(_translate("MainWindow", "Lower Left"))
        self.label_22.setText(_translate("MainWindow", "setpoint (psi)"))
        self.label_23.setText(_translate("MainWindow", "current (psi)"))
        self.label_all.setText(_translate("MainWindow", "0.0"))
        self.groupBox_aul.setTitle(_translate("MainWindow", "Upper Left"))
        self.label_25.setText(_translate("MainWindow", "setpoint (psi)"))
        self.label_26.setText(_translate("MainWindow", "current (psi)"))
        self.label_aul.setText(_translate("MainWindow", "0.0"))
        self.label_t_run.setText(_translate("MainWindow", "0.0"))
        self.label_21.setText(_translate("MainWindow", "(min)"))

