#!/usr/bin/env python3
# import sys
# import numpy as np
# import datetime
# import time
import yaml

from PyQt5.QtWidgets import QWidget, QDoubleSpinBox
from PyQt5 import QtCore

from package.ui	import tunewindow


############################################################
class TuneWindow(QWidget, tunewindow.Ui_Form):

	signal_plotter_closed = QtCore.pyqtSignal()

	def __init__(self, form): #, signal_stop_plot):
		super(self.__class__, self).__init__()
		self.setupUi(self)


		# self.signal_stop_plot = signal_stop_plot

		self.system_params = form.system_params


		# set up spinboxes
		def getDictVal(d, keys):
			n = len(keys)
			if n == 1:
				val = d[keys[0]]
				return float(val)
			else:
				return getDictVal(d[keys[0]], keys[1:])

		for widget in self.children():
			if isinstance(widget, QDoubleSpinBox):
				
				name = widget.objectName()
				keys = name.split('__')[1:]
				val = getDictVal(self.system_params, keys)
				widget.setValue(val)

				widget.valueChanged.connect(self.updateValue)

		# set up button signals/slots
		self.pushButton_save.clicked.connect(self.saveParams)
		self.pushButton_update.clicked.connect(form.updateTiming)


	def updateValue(self):
		def setDictEntry(d, keys, val):
			n = len(keys)
			if n == 1:
				d[keys[0]] = round(val, 3)
			else:
				setDictEntry(d[keys[0]], keys[1:], val)

		name = self.sender().objectName()
		keys = name.split('__')[1:]
		setDictEntry(self.system_params, keys, self.sender().value())


	def saveParams(self):
		with open('system_params.yaml', 'w') as f:
			yaml.dump(self.system_params, f, default_flow_style=False, sort_keys=False)
