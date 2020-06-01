#!/usr/bin/env python3
import sys

import PyQt5
from PyQt5.QtWidgets import *

import mainwindow

class MainWindow(QMainWindow, mainwindow.Ui_MainWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)

		self.doubleSpinBox_chamber1.valueChanged.connect(
			lambda: self.updateChamber(1))
		self.horizontalSlider_chamber1.valueChanged.connect(
			lambda: self.updateChamber(2))

		self.pushButton_start.clicked.connect(lambda: self.runControl(1))
		self.pushButton_stop.clicked.connect(lambda: self.runControl(0))


	def updateChamber(self, n):
		spin_max = self.doubleSpinBox_chamber1.maximum()
		slider_max = self.horizontalSlider_chamber1.maximum()

		if n == 1: # spin box updated
			spin_val = self.doubleSpinBox_chamber1.value()
			self.horizontalSlider_chamber1.setValue(
				spin_val*slider_max/spin_max)
		if n == 2: # slider updated
			slider_val = self.horizontalSlider_chamber1.value()
			self.doubleSpinBox_chamber1.setValue(
				slider_val*spin_max/slider_max)


	def runControl(self, run):
		if run == 1:
			print('running...')
		elif run == 0:
			print('stopped!')





def main():
	app = QApplication(sys.argv)
	form = MainWindow()
	form.show()
	sys.exit(app.exec_())


if __name__ == "__main__":
	main()


# timer after start
# value limit reminders
# get rid of hundredth place
# check bladder on and gray out/set to zero if unchecked
# single on off button (color change? play/stop button)

# killswitch interface for valves/pump --> talk to Drew

# nice to have
# 	status of killswitch
#	diagram of body/highlighting of active chambers


